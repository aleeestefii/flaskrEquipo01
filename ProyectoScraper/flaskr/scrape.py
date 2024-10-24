import requests
from bs4 import BeautifulSoup

def farticles():
    urls = [
        "https://nylonmag.de/digitale-coverstory-mit-riccardo-simonetti-wir-sollten-mehr-licht-ins-dunkel-bringen/",
        "https://nylonmag.de/berlin-streifzug-keen-polly-roche/",
        "https://nylonmag.de/zwischen-blue-jeans-rocknroll-und-milkshakes-wrangler-zelebriert-die-americana-kultur-im-60s-diner-berlin/",
        "https://nylonmag.de/die-kuenstlerinnen-des-slt-space-warum-safer-spaces-in-der-kreativszene-so-wichtig-sind/"
    ]
    articles = []
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        og_title = soup.find('meta', property='og:title')
        og_description = soup.find('meta', property='og:description')
        og_url = soup.find('meta', property='og:url')
        og_site_name = soup.find('meta', property='og:site_name')
        section = soup.find('meta', property='article:section')
        image = soup.find('meta', property='og:image')

        title = og_title['content'] if og_title else 'No title available'
        description = og_description['content'] if og_description else 'No description available'
        url = og_url['content'] if og_url else 'No URL available'
        site_name = og_site_name['content'] if og_site_name else 'No site name found'
        section = section['content'] if section else 'No section found'
        image = image['content'] if image else 'No image found'

        articles.append({
            'title': title,
            'description': description,
            'url': url,
            'site_name': site_name,
            'section': section,
            'main_image_url': image
        })

    return articles

def games():
    URL = "https://vandal.elespanol.com/reportaje/los-23-mejores-juegos-de-2023"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    video_games = []
    juego_elements = soup.find_all("h2", class_="titulo2")
    for juego_element in juego_elements:
        nombre_juego = juego_element.text.strip() if juego_element.text else "Nombre no disponible"
        fecha_element = juego_element.find_next("ul").find("li").text.strip()
        fecha_lanzamiento = fecha_element.replace("Lanzamiento: ", "")
        link_element = juego_element.find_next("ul").find_all("li")[1].find("a")
        link = link_element['href'] if link_element else "Sin enlace"
        video_games.append({
            'game_name': nombre_juego,
            'release_date': fecha_lanzamiento,
            'reason_url': link
        })
    return video_games

def star_info():
    URL = "https://science.nasa.gov/universe/stars/"
    BASE_URL = "https://science.nasa.gov"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    star_elements = soup.find_all("div", class_="GutenbergBlocks hds-module")
    stars = []
    for star_element in star_elements:
        title_element = star_element.find("h2")
        title = title_element.text.strip() if title_element else "Título no disponible"
        image_element = star_element.find("img")
        image_url = image_element["src"] if image_element else "No image"
        category = "Star Basics"
        learn_more_element = star_element.find("a")
        if learn_more_element:
            learn_more_link = learn_more_element["href"]
            if learn_more_link.startswith("/"):
                learn_more_link = BASE_URL + learn_more_link
        else:
            learn_more_link = "No link"
        stars.append(
            {
                "title": title,
                "image_url": image_url,
                "category": category,
                "learn_more": learn_more_link,
            }
        )
    return stars

