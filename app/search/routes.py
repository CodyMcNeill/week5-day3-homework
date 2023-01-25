from flask import render_template, request, redirect, url_for, Blueprint
from .forms import searchPoke
from .services import get_poke_info

search = Blueprint('search', __name__)

@search.route('/pokedex', methods=['GET', 'POST'])
def pokedexPage():
    form = searchPoke()
    if request.method == 'POST':
        if form.validate_on_submit():
            search = form.searchBody.data.lower()
            print(get_poke_info(search))
            return get_poke_info(search)
    return render_template('pokedex.html', form = form)