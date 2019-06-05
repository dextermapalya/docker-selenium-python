# Distributed Testing with Selenium Grid and Docker

Distribute automated tests with Selenium Grid and Docker Swarm

### Want to learn how to build this?

Check out the [post](https://testdriven.io/distributed-testing-with-selenium-grid).

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment

1. Install the requirements using pip

    ```
       export BROWSER=chrome
       export NODE_HUB_ADDRESS=
    ```

1) Git clone url
2) export BROWSER=chrome
3) export NODE_HUB_ADDRESS=
4) virtualenv -p python3 venv
5) pip install -r requirements.txt
6) source venv/bin/activate
5) cd project
6) python sunnxt.py



    ```sh
    $ sh project/create.sh
    ```

1. Set the environment variable:

    ```sh
    $ eval $(docker-machine env node-1)
    $ NODE=$(docker service ps --format "{{.Node}}" selenium_hub)
    $ export NODE_HUB_ADDRESS=$(docker-machine ip $NODE)
    ```

1. Run the tests:

    ```sh
    $ python project/parallel_test_run.py
    ```

1. Bring down the resources:

    ```sh
    $ sh project/destroy.sh
    ```
