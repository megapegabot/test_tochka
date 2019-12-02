--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0 (Debian 12.0-2.pgdg100+1)
-- Dumped by pg_dump version 12.0 (Debian 12.0-2.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: users; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.users (
    uuid uuid DEFAULT public.uuid_generate_v4(),
    fio character varying(225) NOT NULL,
    hold integer NOT NULL,
    current_balans integer NOT NULL,
    status boolean DEFAULT true
);


ALTER TABLE public.users OWNER TO "user";

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.users (uuid, fio, hold, current_balans, status) FROM stdin;
9c9bf9f0-dfbe-4961-acf8-bc8c67bb00dd	string	0	564750	t
1e30226b-a7e8-406f-9c98-ff87dde0629e	string	0	565574	t
856209e5-02c0-4682-b72c-627fe7fc2dc4	string	0	565792	t
48f97256-af8b-4dbb-aa6c-5de88fe582cf	string	0	566990	t
b295ce14-bad1-4dff-9198-dc42ce3bcdf3	string	0	566126	t
d118f561-c863-4c3b-b5d0-b283fe9edbd4	string	0	566348	t
e4641e7e-3ea8-4abe-a6ca-87a892d8f1e6	string	0	566860	t
6223f859-105e-4892-8f8f-ebf81badf593	string	0	565626	t
aea25253-ece4-4573-9cab-9a67b66d5fd4	string	0	566154	t
5dc0a93a-8307-4e4b-9171-76ce2cee5130	string	0	565992	t
71350d66-733b-4b14-a3a8-a6d90e301971	string	0	566144	t
755956ad-fbe8-4a77-ada2-da316deda5d8	string	0	566056	t
720f418e-7afa-4f64-a65d-742f74b0d016	string	0	566858	t
5adf2735-782f-4532-8436-3b4be3fb5915	string	0	565982	t
7d3e8a69-1a9e-4fae-8b02-34fb830e0385	string	0	566200	t
b2893223-8bb0-4691-8f04-32ddb00ea23f	string	0	566384	t
c46e47f8-1b61-46f9-ba72-ed814351cf8d	string	0	566684	t
82e17e3c-bec0-4a4d-8392-d5776322221a	string	0	567048	t
faa46e00-d8ee-4cf9-9376-1b86d440fbc6	string	0	10566059	t
5e2bb76b-dda3-4c9a-9082-e08e9c2fdcc1	test	0	-1177	t
047578d2-e843-4df7-817d-3a8a540ab75d	Станислав Рычков	0	-1000	t
f555cea8-2ccd-4153-98ac-babefd9ac543	string	0	606494	t
8d588f8b-8831-4fb6-8835-f3ac05cf974a	string	0	636969	t
\.


--
-- PostgreSQL database dump complete
--

