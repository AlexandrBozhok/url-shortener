import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import exc

from crud.link import LinkCRUD
from config.db import db_session
from utils.enums import LinkFilterBy
from utils.helpers import extract_model_id_from_url_alias

router = Blueprint('router', __name__)


@router.get('/')
def index():
    return render_template('index.html')


@router.get('/<short_url>')
def redirect_to_own_url(short_url: str):
    link_id = extract_model_id_from_url_alias(short_url)

    link_db = LinkCRUD.get_one(
        by=LinkFilterBy.ID,
        value=link_id,
        session=db_session
    )
    if not link_db:
        return redirect(url_for('router.index'))
    return redirect(link_db.original_url)


@router.post('/add_link')
def add_link():
    original_url = request.form['original_url']

    link_db = LinkCRUD.get_one(
        by=LinkFilterBy.original_url,
        value=original_url,
        session=db_session
    )
    if not link_db:
        try:
            link_db = LinkCRUD.create(
                original_url=original_url,
                session=db_session
            )
        except exc.SQLAlchemyError as e:
            logging.error(f'Error: {e}')
            return 'Ooops', 500

    return render_template(
        'link_added.html',
        new_link=link_db.short_url,
        original_url=link_db.original_url
    )
