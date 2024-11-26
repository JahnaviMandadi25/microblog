from flask import current_app


def add_to_index(index, model):
    """
    Add a document to an Elasticsearch index.
    :param index: Name of the index.
    :param model: The model instance to be indexed.
    """
    if not current_app.elasticsearch:
        current_app.logger.warning("Elasticsearch is not configured.")
        return
    payload = {field: getattr(model, field) for field in getattr(model, '__searchable__', [])}
    try:
        current_app.elasticsearch.index(index=index, id=model.id, document=payload)
        current_app.logger.info(f"Document added to index: {index}, ID: {model.id}")
    except Exception as e:
        current_app.logger.error(f"Failed to add document to index: {e}")


def remove_from_index(index, model):
    """
    Remove a document from an Elasticsearch index.
    :param index: Name of the index.
    :param model: The model instance to be removed.
    """
    if not current_app.elasticsearch:
        current_app.logger.warning("Elasticsearch is not configured.")
        return
    try:
        current_app.elasticsearch.delete(index=index, id=model.id)
        current_app.logger.info(f"Document removed from index: {index}, ID: {model.id}")
    except Exception as e:
        current_app.logger.error(f"Failed to remove document from index: {e}")


def query_index(index, query, page, per_page):
    """
    Perform a search query on an Elasticsearch index.
    :param index: Name of the index.
    :param query: The search query string.
    :param page: Current page number.
    :param per_page: Number of results per page.
    :return: A tuple containing a list of IDs and the total number of results.
    """
    if not current_app.elasticsearch:
        current_app.logger.warning("Elasticsearch is not configured.")
        return [], 0

    try:
        search = current_app.elasticsearch.search(
            index=index,
            query={'multi_match': {'query': query, 'fields': ['*']}},
            from_=(page - 1) * per_page,
            size=per_page
        )
        ids = [int(hit['_id']) for hit in search['hits']['hits']]
        total = search['hits']['total']['value']
        current_app.logger.info(f"Query successful on index: {index}, Query: {query}")
        return ids, total
    except Exception as e:
        current_app.logger.error(f"Failed to query index: {e}")
        return [], 0
