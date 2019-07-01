from flask import (Blueprint,
                   render_template,
                   redirect,
                   url_for,
                   request,
                   session)
from models.reviews import Review

main = Blueprint('index', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/submit/<int:id>', methods=['POST', 'GET'])
def submit(id):
    if request.method == 'POST':
        form = request.form
        review = Review.new(form)
        review.get_classification()
        review.save()
        return redirect(url_for('index.submit', review=review, id=review.id))
    review = Review.find(id=id)
    return render_template('result.html', review=review)


@main.route('/return_right', methods=['POST'])
def return_right():
    return redirect(url_for('index.thanks'))


@main.route('/return_wrong', methods=['POST'])
def return_wrong():
    id = request.args.get('id')
    review = Review.find(id=int(id))
    print(id, review)
    if review.classification == 'Positive':
        review.classification = 'Negative'
    else:
        review.classification = 'Positive'
    review.save()
    return redirect(url_for('index.thanks'))


@main.route('/thanks')
def thanks():
    return render_template('thanks.html')
