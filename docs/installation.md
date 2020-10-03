# Installation

* [Fork repository][IWrok Test] and clone it.

=== "Shell or CMD"
    <div class="termy">
    ```console
    $ git clone https://github.com/Mohamed-Kaizen/IWork-test
    
    ---> 100%

    Done :)
    ```
    </div>


### install dependence

=== "Poetry"
    <div class="termy">
    ```console
    $ cd IWork-test
    $ poetry install
    
    Resolving dependencies... 
    ---> 100%

    Writing lock file

    Done :)
    ```
    </div>

=== "Pip"
    <div class="termy">
    ```console
    $ cd IWork-test
    $ pip install -r requirements.txt
    
    ---> 100%

    Done :)
    ```
    </div>

### Environment Variables

create .env in the root of the project or set your ENV add the following line into .env file or set your ENV:
    
    DEBUG=True  # change this in production
    ALLOWED_HOSTS=example.com, localhost, 0.0.0.0, 127.0.0.1  # change this in production
    SECRET_KEY=w86k@*ash*z)dsxsoz+o*ne*ugb08(4nu13%8!m*+2_e@@7hnx  # change this in production and never put the production key here
    DATABASE_URL=sqlite:///db.sqlite3
    EMAIL_USER=example@example.com
    EMAIL_PASSWORD=''


[IWrok Test]: https://github.com/Mohamed-Kaizen/IWork-test
 

