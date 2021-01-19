from flask import redirect, render_template, url_for, request, abort, flash, Blueprint
from flask_login import login_required, current_user
from app import db
from app.models import Post
from app.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html',title='New Post', form=form, legend='New Post')

@posts.route("/post/<int:post_id>")   #to route a post with its post_id
def post(post_id):
    post = Post.query.get_or_404(post_id)   #returns 404 error if post not founds
    return render_template('post.html',title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data        #add the new/edited data to title
        post.content = form.content.data    #add new data to content
        db.session.commit()                 #commit changes
        flash('Your post has been updated!','success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                            form=form, legend='Update Post')

@posts.route('/post/<int:post_id>/delete', methods=['POST'])  #Only POST method, after the delete submission
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!','success')
    return redirect(url_for('main.home'))