from flask import Blueprint, render_template, request, redirect, url_for
from .models import Link
from .extensions import db
short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.visits = link.visits + 1
    db.session.commit()
    if 'https://' in link.original_url or "http://" in link.original_url:
        return redirect(link.original_url)
    return redirect("https://" + link.original_url)

@short.route('/')
def index():
    return render_template('index.html')

@short.route('/add_link', methods=['GET', 'POST'])
def add_link():
    if request.method == 'POST':
        original_url = request.form['original_url']
        row = db.session.query(Link).filter_by(original_url=original_url).first()
        if not row:
            link = Link(original_url=original_url)
            db.session.add(link)
            db.session.commit()
            return render_template('link_added.html', 
                new_link=link.short_url, original_url=link.original_url)
            #return redirect(url_for('short.add_link'), code='303')
        else:
            return render_template('link_added.html', 
                new_link=row.short_url, original_url=row.original_url)
            #return redirect(url_for('short.add_link'), code='303')
    else:
        return render_template('link_added.html', new_link=None)
    

@short.route('/stats')
def stats():
    pass

@short.errorhandler(404)
def page_not_found(e):
    return '', 404