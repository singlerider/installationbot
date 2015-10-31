--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: twitchinstalls; Type: DATABASE; Schema: -; Owner: shane
--

CREATE DATABASE twitchinstalls WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE twitchinstalls OWNER TO shane;

\connect twitchinstalls

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: messages; Type: TABLE; Schema: public; Owner: shane; Tablespace: 
--

CREATE TABLE messages (
    username character varying(50) DEFAULT ''::character varying NOT NULL,
    message character varying(2000) DEFAULT ''::character varying NOT NULL,
    time_stamp double precision NOT NULL
);


ALTER TABLE messages OWNER TO shane;

--
-- Name: users; Type: TABLE; Schema: public; Owner: shane; Tablespace: 
--

CREATE TABLE users (
    username character varying(50) DEFAULT ''::character varying NOT NULL,
    points integer NOT NULL,
    time_in_chat integer NOT NULL
);


ALTER TABLE users OWNER TO shane;

--
-- Name: messages_pkey; Type: CONSTRAINT; Schema: public; Owner: shane; Tablespace: 
--

ALTER TABLE ONLY messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (username, time_stamp);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: shane; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (username);


--
-- Name: messages; Type: FK CONSTRAINT; Schema: public; Owner: shane
--

ALTER TABLE ONLY messages
    ADD CONSTRAINT messages FOREIGN KEY (username) REFERENCES users(username);


--
-- Name: public; Type: ACL; Schema: -; Owner: shane
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM shane;
GRANT ALL ON SCHEMA public TO shane;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

