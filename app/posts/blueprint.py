from flask import Blueprint
from flask import render_template
from flask_login import current_user

from models import Post
from .forms import PostForm

from flask import request
from app import db

from flask import redirect
from flask import url_for

from flask_security import login_required

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        name = current_user.name
        body = request.form['body']
        mark = request.form["inlineRadioOptions"]
        try:
            post = Post(name=name, body=body, mark=mark)
            db.session.add(post)
            db.session.commit()
        except:
            print('Что-то пошло не так!')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    posts = Post.query
    pages = posts.paginate(page=page, per_page=12)

    return render_template('posts/index.html', posts=posts, pages=pages)



