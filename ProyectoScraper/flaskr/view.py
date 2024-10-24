from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()

    fashion_articles = []
    video_games = []
    star_infos = []


    if g.user:
        selected_sites = g.user['selected_sites']

        if 'fashion_article' in selected_sites:
            fashion_articles = db.execute(
                'SELECT id, title, description, url, site_name, section, main_image_url'
                ' FROM fashion_article'
                ' ORDER BY id DESC'
            ).fetchall()
        if 'video_game' in selected_sites:
            video_games = db.execute(
                'SELECT id, game_name, release_date, reason_url'
                ' FROM video_game'
                ' ORDER BY id DESC'
            ).fetchall()
        if 'star_info' in selected_sites:
            star_infos = db.execute(
                'SELECT id, title, image_url, category, learn_more'
                ' FROM star_info'
                ' ORDER BY id DESC'
            ).fetchall()
    else:
        fashion_articles = db.execute(
            'SELECT id, title, description, url, site_name, section, main_image_url'
            ' FROM fashion_article'
            ' ORDER BY id DESC'
        ).fetchall()
        video_games = db.execute(
            'SELECT id, game_name, release_date, reason_url'
            ' FROM video_game'
            ' ORDER BY id DESC'
        ).fetchall()
        star_infos = db.execute(
            'SELECT id, title, image_url, category, learn_more'
            ' FROM star_info'
            ' ORDER BY id DESC'
        ).fetchall()

    return render_template(
        'blog/index.html', 
        fashion_articles=fashion_articles, 
        video_games=video_games, 
        star_infos=star_infos
    )
