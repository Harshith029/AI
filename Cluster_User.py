import random
from geopy.distance import geodesic # type: ignore

def cluster_users(self, users: list, num_clusters: int = 3) -> list:
    """
    Group users by destination similarity using custom clustering.

    Args:
        users (list): List of user dicts with 'dest_lat' and 'dest_lon'.
        num_clusters (int): Number of clusters to form.

    Returns:
        list: Same users with an added 'cluster' key.
    """
    if len(users) <= num_clusters:
        for i, user in enumerate(users):
            user['cluster'] = i
        return users

    # Randomly initialize cluster centers
    centers = random.sample(users, num_clusters)
    centroids = [(c['dest_lat'], c['dest_lon']) for c in centers]

    for user in users:
        distances = [geodesic((user['dest_lat'], user['dest_lon']), center).km for center in centroids]
        user['cluster'] = distances.index(min(distances))

    return users
