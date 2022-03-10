from locust import HttpUser
from locustodoorpc import OdooRPCLocust
from tasks import (
    BackendReadOnlyBehavior,
    BackendWriteOnlyBehavior,
    BackendMixedBehavior,
    FrontendBehavior,
)


class BackendReadOnlyUser(OdooRPCLocust):
    min_wait = 500
    max_wait = 5000
    weight = 10

    tasks = [BackendReadOnlyBehavior]


class BackendWriteOnlyUser(OdooRPCLocust):
    min_wait = 800
    max_wait = 5000
    weight = 1

    tasks = [BackendWriteOnlyBehavior]


class BackendMixedUser(OdooRPCLocust):
    min_wait = 500
    max_wait = 3000
    weight = 5

    tasks = [BackendMixedBehavior]


class FrontendUser(HttpUser):
    min_wait = 200
    max_wait = 5000
    weight = 5

    tasks = [FrontendBehavior]
