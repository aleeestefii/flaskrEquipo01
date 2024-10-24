import click
from .db import get_db, close_db, init_app
from .scrape import farticles, games, star_info
from flask import Flask

app = Flask(__name__)
app.config['DATABASE'] = 'schema.sql'

init_app(app)

@click.command('scrape')
def scrape():
    db = get_db()

    fashion_articles = farticles()
    for article in fashion_articles:
        db.execute(
            'INSERT INTO fashion_article (title, description, url, site_name, section, main_image_url) VALUES (?, ?, ?, ?, ?, ?)',
            (article['title'], article['description'], article['url'], article['site_name'], article['section'], article['main_image_url'])
        )

    video_games = games()
    for game in video_games:
        db.execute(
            'INSERT INTO video_game (game_name, release_date, reason_url) VALUES (?, ?, ?)',
            (game['game_name'], game['release_date'], game['reason_url'])
        )

    star_infow = star_info()
    for star in star_infow:
        db.execute(
            'INSERT INTO star_info (title, image_url, category, learn_more) VALUES (?, ?, ?, ?)',
            (star['title'], star['image_url'], star['category'], star['learn_more'])
        )
    
    db.commit()
    close_db()
    click.echo("Scraping completado y datos guardados en la base de datos.")

app.cli.add_command(scrape)

if __name__ == '__main__':
    app.run(debug=True)
