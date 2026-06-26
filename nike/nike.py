import os
import json
import asyncio # Indispensable pour le mode __main__ à la fin
from playwright.async_api import async_playwright # Remplacement par async
from colors import *
from nike_product import *
from discord_webhook import DiscordWebhook

url = "https://www.nike.com/fr/"
jsonFind = False

# Bloquer les images (Inchangé mais asynchrone pour Playwright)
async def block_img(route):
    if route.request.resource_type == "image":
        return await route.abort()
    return await route.continue_()

# getStockInfos reste synchrone car elle traite des données en mémoire, pas du réseau
async def getStockInfos(response):
    if "api" in response.url or "graphql" in response.url:
        if response.status == 200:
            try:
                content_type = response.headers.get("content-type", "")
                if "application/json" in content_type:
                    data = await response.json()
                    str_data = str(data).lower()
                    if "available" in str_data or "sku" in str_data:
                        if os.path.exists('nike_stock_data.json'):
                            return
                        print(f"\n[JSON TROUVÉ] URL: {response.url[:80]}...")
                        with open("nike_stock_data.json", "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
                        print("Fichier nike_stock_data.json enregistré !\n")
                        return 
            except Exception as e:
                pass

def sendWeb(embed):
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/...")
    webhook.add_embed(embed)
    webhook.execute()


# 1. On déclare la fonction principale en ASYNC
async def run(pw, input):
    # 2. Ajout de AWAIT devant launch
    browser = await pw.firefox.launch(headless=True)
    print(f"{MAGENTA}browser start{RESET}\n")
    
    # 3. Ajout de AWAIT devant new_page
    page = await browser.new_page()

    # Si tu réactives le blocage d'images, utilise await :
    # await page.route("**/*", block_img)

    page.on("response", getStockInfos)
    
    # 4. Ajout de AWAIT devant goto
    await page.goto(url)
    print(f"{MAGENTA}page load{RESET}\n")

    # 5. Ajout de AWAIT devant toutes les actions de page / locator
    cookies_accept = page.get_by_test_id("modal-accept-button")
    await cookies_accept.wait_for(state="visible", timeout=15000)
    await cookies_accept.click()

    # Remplacement de wait_for_timeout par des await
    await page.wait_for_timeout(2500)
    await page.get_by_role("searchbox", name="Rechercher des produits").click()
    await page.wait_for_timeout(2000)
    await page.get_by_role("searchbox", name="Rechercher des produits").fill(input)
    await page.wait_for_timeout(5000)
    await page.get_by_role("searchbox", name="Rechercher des produits").press("Enter")
    
    shoePage = page.locator('a[data-testid="product-card__link-overlay"]').first
    await shoePage.wait_for(state="attached", timeout=30000)
    
    toSend = "Empty"
    # count() est aussi asynchrone maintenant !
    if await shoePage.count() > 0:
        await shoePage.click(force=True)
        await page.wait_for_selector("#pdp_product_title", state="visible", timeout=15000)
        await page.wait_for_timeout(5000)
        
        # page.content() nécessite un await
        html_content = await page.content()
        toSend = get_product(html=html_content)
    else:
        toSend = "No valid product !"
        print(f"{RED}No product find !{RESET}\n")
        
    # 6. Ajout de AWAIT pour la fermeture
    await browser.close()
    print(f"{MAGENTA}browser closed{RESET}\n")
    return toSend


# 7. Modification du bloc de test pour pouvoir lancer le script tout seul en async
if __name__ == '__main__':
    choice = input("Enter Shoes name : ")
    
    async def main():
        async with async_playwright() as play:
            await run(pw=play, input=choice)
            
    asyncio.run(main())