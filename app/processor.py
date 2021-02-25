from app.utils import get_substitutions_templates


def variables_processor(request=None):
    c = get_substitutions_templates(request=request)
    from news.utils import get_latest_articles
    from event.utils import get_future_events
    from event.utils import get_past_events
    from user.utils import get_organisers, get_board
    from page.utils import get_menu_pages

    c["articles"] = get_latest_articles()
    c["events"] = {"future": get_future_events(), "past": get_past_events()}
    c["organisers"] = get_organisers()
    c["board"] = get_board()
    c["categories"] = get_menu_pages()
    return c
