import requests
""" HTTP GET """
url = "https://yts.mx/api/v2/list_movies.json"

"""
:param <int> limit: limit result per page (1-50)
:param <int> page: show result of the next page (Default=1)
:param <str> quality: filter by quality, option=(720p, 1080p, 2160p, 3D, All), (Default=All)
:param <int> minimum_rating: filter movie by minimum_rating (0-9)
:param <str> query_term: Used for movie search, 
             matching on: Movie Title/IMDb Code, Actor Name/IMDb Code,
             Director Name/IMDb Code
:param <str> genre: Used to filter by a given genre
:param <str> sort_by: Sorts the results by chosen value
             (title, year, rating, peers, seeds, download_count, like_count, date_added)
:param <str> order_by: Orders the results by either Ascending or Descending order
             (desc, asc)
:param <bool> with_rt_ratings: Returns the list with the Rotten Tomatoes rating included
"""

def home_page():
    """
    :return <dict> data: movies data
    """
    try:
        req = requests.request(
            method="GET",
            url=f"{url}"
        )
    except Exception as err:
        return {
            "status": False,
            "message": f"{err}"
        }
    else:
        res = req.json()
        if res['status'] == "ok" and "movies" in res['data']:
            return {
                "data": res['data']['movies'],
                "status": True
            }
        else:
            return {
                "status": False,
                "message": "Error! Please check with your HelpDesk!"
            }

def next_page(cur_page):
    """
    :param cur_page: current page
    :return <dict> data: movies data
    """
    try:
        req = requests.request(
            method="GET",
            url=f"{url}?page={int(cur_page+1)}"
        )
    except Exception as err:
        return {
            "status": False,
            "message": f"{err}"
        }
    else:
        res = req.json()
        if res['status'] == "ok" and "movies" in res['data']:
            return {
                "data": res['data']['movies'],
                "status": True
            }
        else:
            return {
                "status": False,
                "message": "Error! Please check with your HelpDesk!"
            }

def default_action():
    """
    :return <dict> data: action movies data
    """
    try:
        req = requests.request(
            method="GET",
            url=f"{url}?genre=action"
        )
    except Exception as err:
        return {
            "status": False,
            "message": f"{err}"
        }
    else:
        res = req.json()
        if res['status'] == "ok" and "movies" in res['data']:
            return {
                "data": res['data']['movies'],
                "status": True
            }
        else:
            return {
                "status": False,
                "message": "Error! Please check with your HelpDesk!"
            }

def search_result(title):
    """
    :param <str> title: Title of the movie to be searched
    :return: status True if success and movies detail will be in "data"
    """
    try:
        req = requests.request(
            method="GET",
            url=f"{url}?query_term={title}"
        )
    except Exception as err:
        return {
            "status": False,
            "message": f"{err}"
        }
    else:
        res = req.json()
        if res['status'] == "ok" and "movies" in res['data']:
            return {
                "data": res['data']['movies'],
                "status": True
            }
        else:
            return {
                "status": False,
                "message": "No movies found!"
            }

