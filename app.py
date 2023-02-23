from petfax import create_app
app=create_app()
url_for('static', filename='style.css')

bp = Blueprint(
    'pet',
    __name__,
    url_prefix='/pets'
)

@bp.route('/')
def index():
    return 'Here are all the posts' 
