CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        username VARCHAR(144) NOT NULL, 
        passwordhash VARCHAR(144) NOT NULL, 
        role VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);
CREATE TABLE poll (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        description VARCHAR(280), 
        upvotes INTEGER NOT NULL, 
        downvotes INTEGER NOT NULL, 
        neutralvotes INTEGER NOT NULL, 
        done BOOLEAN NOT NULL, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (done IN (0, 1)), 
        FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE group (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        created_by INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(created_by) REFERENCES account (id)
);
CREATE TABLE poll_account_link (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        userid INTEGER, 
        pollid INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(userid) REFERENCES account (id), 
        FOREIGN KEY(pollid) REFERENCES poll (id)
);
CREATE TABLE group_account_link (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        group_id INTEGER, 
        account_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(group_id) REFERENCES "group" (id), 
        FOREIGN KEY(account_id) REFERENCES account (id)
);
