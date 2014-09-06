CREATE TABLE IF NOT EXISTS hon_user(
    id serial NOT NULL PRIMARY KEY,

    username text NOT NULL UNIQUE,
    password text NOT NULL,
    creation_date timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS hon_account(
    id serial NOT NULL PRIMARY KEY,

    name text NOT NULL,
    user_id bigint NOT NULL REFERENCES hon_user(id),
    creation_date timestamp NOT NULL,

    UNIQUE (name, user_id)
);

CREATE TABLE IF NOT EXISTS hon_transaction(
    id serial NOT NULL PRIMARY KEY,

    name text NOT NULL,
    value decimal(10, 2) NOT NULL,
    description text,
    account_id bigint NOT NULL REFERENCES hon_account(id),
    transaction_date timestamp NOT NULL,
    creation_date timestamp NOT NULL
);

CREATE OR REPLACE VIEW hon_transaction_view AS
SELECT t.id, t.name, value, description, account_id,
       a.name account_name, transaction_date, t.creation_date
FROM hon_transaction t
JOIN hon_account a on t.account_id = a.id
