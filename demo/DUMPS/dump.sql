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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO dogspot;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO dogspot;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO dogspot;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO dogspot;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO dogspot;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO dogspot;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE authtoken_token (
    key character varying(40) NOT NULL,
    user_id integer NOT NULL,
    created timestamp with time zone NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO dogspot;

--
-- Name: demo_dog; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_dog (
    id integer NOT NULL,
    name character varying(254) NOT NULL,
    sex boolean NOT NULL,
    bred character varying(254) NOT NULL,
    comment character varying(254) NOT NULL
);


ALTER TABLE public.demo_dog OWNER TO dogspot;

--
-- Name: demo_dog_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_dog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_dog_id_seq OWNER TO dogspot;

--
-- Name: demo_dog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_dog_id_seq OWNED BY demo_dog.id;


--
-- Name: demo_dogspotuser; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_dogspotuser (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    email character varying(255) NOT NULL,
    mail_verified boolean NOT NULL,
    is_active boolean NOT NULL,
    is_admin boolean NOT NULL
);


ALTER TABLE public.demo_dogspotuser OWNER TO dogspot;

--
-- Name: demo_dogspotuser_groups; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_dogspotuser_groups (
    id integer NOT NULL,
    dogspotuser_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.demo_dogspotuser_groups OWNER TO dogspot;

--
-- Name: demo_dogspotuser_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_dogspotuser_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_dogspotuser_groups_id_seq OWNER TO dogspot;

--
-- Name: demo_dogspotuser_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_dogspotuser_groups_id_seq OWNED BY demo_dogspotuser_groups.id;


--
-- Name: demo_dogspotuser_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_dogspotuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_dogspotuser_id_seq OWNER TO dogspot;

--
-- Name: demo_dogspotuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_dogspotuser_id_seq OWNED BY demo_dogspotuser.id;


--
-- Name: demo_dogspotuser_user_permissions; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_dogspotuser_user_permissions (
    id integer NOT NULL,
    dogspotuser_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.demo_dogspotuser_user_permissions OWNER TO dogspot;

--
-- Name: demo_dogspotuser_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_dogspotuser_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_dogspotuser_user_permissions_id_seq OWNER TO dogspot;

--
-- Name: demo_dogspotuser_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_dogspotuser_user_permissions_id_seq OWNED BY demo_dogspotuser_user_permissions.id;


--
-- Name: demo_emailverification; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_emailverification (
    id integer NOT NULL,
    verification_key character varying(21) NOT NULL,
    key_timestamp timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.demo_emailverification OWNER TO dogspot;

--
-- Name: demo_emailverification_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_emailverification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_emailverification_id_seq OWNER TO dogspot;

--
-- Name: demo_emailverification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_emailverification_id_seq OWNED BY demo_emailverification.id;


--
-- Name: demo_opinion; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_opinion (
    raiting_id integer NOT NULL,
    opinion_text character varying(500) NOT NULL
);


ALTER TABLE public.demo_opinion OWNER TO dogspot;

--
-- Name: demo_opinionusefulnessrating; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_opinionusefulnessrating (
    id integer NOT NULL,
    opinion_id integer NOT NULL,
    user_id integer NOT NULL,
    vote integer NOT NULL
);


ALTER TABLE public.demo_opinionusefulnessrating OWNER TO dogspot;

--
-- Name: demo_opinionusefulnessrating_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_opinionusefulnessrating_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_opinionusefulnessrating_id_seq OWNER TO dogspot;

--
-- Name: demo_opinionusefulnessrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_opinionusefulnessrating_id_seq OWNED BY demo_opinionusefulnessrating.id;


--
-- Name: demo_otofoto; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_otofoto (
    id integer NOT NULL,
    title character varying(254) NOT NULL,
    obrazek character varying(100) NOT NULL
);


ALTER TABLE public.demo_otofoto OWNER TO dogspot;

--
-- Name: demo_otofoto_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_otofoto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_otofoto_id_seq OWNER TO dogspot;

--
-- Name: demo_otofoto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_otofoto_id_seq OWNED BY demo_otofoto.id;


--
-- Name: demo_raiting; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_raiting (
    id integer NOT NULL,
    data_added timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    spot_id integer NOT NULL,
    dogs_allowed boolean NOT NULL,
    friendly_rate integer NOT NULL,
    CONSTRAINT demo_raiting_friendly_rate_check CHECK ((friendly_rate >= 0))
);


ALTER TABLE public.demo_raiting OWNER TO dogspot;

--
-- Name: demo_raiting_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_raiting_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_raiting_id_seq OWNER TO dogspot;

--
-- Name: demo_raiting_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_raiting_id_seq OWNED BY demo_raiting.id;


--
-- Name: demo_spot; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_spot (
    id integer NOT NULL,
    name character varying(250) NOT NULL,
    latitude numeric(8,5) NOT NULL,
    longitude numeric(8,5) NOT NULL,
    mpoint geometry(Point,4326),
    address_street character varying(254) NOT NULL,
    address_number character varying(10) NOT NULL,
    address_city character varying(100) NOT NULL,
    address_country character varying(100) NOT NULL,
    spot_type integer NOT NULL,
    is_accepted boolean NOT NULL,
    phone_number character varying(100) NOT NULL,
    email character varying(75),
    www character varying(200),
    facebook character varying(254),
    dogs_allowed boolean,
    friendly_rate numeric(3,2)
);


ALTER TABLE public.demo_spot OWNER TO dogspot;

--
-- Name: demo_spot_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_spot_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_spot_id_seq OWNER TO dogspot;

--
-- Name: demo_spot_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_spot_id_seq OWNED BY demo_spot.id;


--
-- Name: demo_usersspotslist; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE demo_usersspotslist (
    id integer NOT NULL,
    data_added timestamp with time zone NOT NULL,
    spot_id integer NOT NULL,
    user_id integer NOT NULL,
    role integer NOT NULL
);


ALTER TABLE public.demo_usersspotslist OWNER TO dogspot;

--
-- Name: demo_usersspotslist_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE demo_usersspotslist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demo_usersspotslist_id_seq OWNER TO dogspot;

--
-- Name: demo_usersspotslist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE demo_usersspotslist_id_seq OWNED BY demo_usersspotslist.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO dogspot;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO dogspot;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO dogspot;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: dogspot
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO dogspot;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dogspot
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: dogspot; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO dogspot;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_dog ALTER COLUMN id SET DEFAULT nextval('demo_dog_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_dogspotuser ALTER COLUMN id SET DEFAULT nextval('demo_dogspotuser_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_dogspotuser_groups ALTER COLUMN id SET DEFAULT nextval('demo_dogspotuser_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_dogspotuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('demo_dogspotuser_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_emailverification ALTER COLUMN id SET DEFAULT nextval('demo_emailverification_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_opinionusefulnessrating ALTER COLUMN id SET DEFAULT nextval('demo_opinionusefulnessrating_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_otofoto ALTER COLUMN id SET DEFAULT nextval('demo_otofoto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_raiting ALTER COLUMN id SET DEFAULT nextval('demo_raiting_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_spot ALTER COLUMN id SET DEFAULT nextval('demo_spot_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_usersspotslist ALTER COLUMN id SET DEFAULT nextval('demo_usersspotslist_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('auth_permission_id_seq', 9, true);


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY authtoken_token (key, user_id, created) FROM stdin;
\.


--
-- Data for Name: demo_dog; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_dog (id, name, sex, bred, comment) FROM stdin;
1	Rubi	f	labrador	instagram.com/_________rubi
2	ążśćńłóńę	f	not specifiedff	rf
\.


--
-- Name: demo_dog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_dog_id_seq', 2, true);


--
-- Data for Name: demo_dogspotuser; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_dogspotuser (id, password, last_login, is_superuser, email, mail_verified, is_active, is_admin) FROM stdin;
12	pbkdf2_sha256$12000$aVUUqgH1PXKu$hJ/Prepoj3kENsYtk/lewPHgj1xBuLk8ozHWoSCPhqA=	2014-10-03 18:01:24.464174+00	f	andrzej.kostanski@gmail.com	t	t	f
13	pbkdf2_sha256$12000$0HMivgpENSuJ$D8MqYnVA4q3zwLS2P0DSMQlOVPelIHg2gqPlSjXMSJU=	2014-10-23 10:27:12.625293+00	f	andrzej.kostanski@daftcode.pl	t	t	f
14	pbkdf2_sha256$12000$VJGwpxROwj4H$EgskHuwLDsnu6GFdBelHGvb3iGcRXPT0tZekM8toXA0=	2014-10-25 19:19:55.941058+00	f	weronikaas@gmail.com	t	t	f
\.


--
-- Data for Name: demo_dogspotuser_groups; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_dogspotuser_groups (id, dogspotuser_id, group_id) FROM stdin;
\.


--
-- Name: demo_dogspotuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_dogspotuser_groups_id_seq', 1, false);


--
-- Name: demo_dogspotuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_dogspotuser_id_seq', 14, true);


--
-- Data for Name: demo_dogspotuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_dogspotuser_user_permissions (id, dogspotuser_id, permission_id) FROM stdin;
\.


--
-- Name: demo_dogspotuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_dogspotuser_user_permissions_id_seq', 1, false);


--
-- Data for Name: demo_emailverification; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_emailverification (id, verification_key, key_timestamp, user_id) FROM stdin;
12	Kl5g70t_TTqwWyLOdlwrW	2014-10-03 18:01:09.115763+00	12
13	hfVkMCJhRbSPFDpQN6Pif	2014-10-23 10:26:31.86618+00	13
14	FyYME7KyQL2V1jCYQf9ZJ	2014-10-25 19:19:55.995016+00	14
\.


--
-- Name: demo_emailverification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_emailverification_id_seq', 14, true);


--
-- Data for Name: demo_opinion; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_opinion (raiting_id, opinion_text) FROM stdin;
\.


--
-- Data for Name: demo_opinionusefulnessrating; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_opinionusefulnessrating (id, opinion_id, user_id, vote) FROM stdin;
\.


--
-- Name: demo_opinionusefulnessrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_opinionusefulnessrating_id_seq', 1, false);


--
-- Data for Name: demo_otofoto; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_otofoto (id, title, obrazek) FROM stdin;
\.


--
-- Name: demo_otofoto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_otofoto_id_seq', 1, false);


--
-- Data for Name: demo_raiting; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_raiting (id, data_added, user_id, spot_id, dogs_allowed, friendly_rate) FROM stdin;
\.


--
-- Name: demo_raiting_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_raiting_id_seq', 3, true);


--
-- Data for Name: demo_spot; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_spot (id, name, latitude, longitude, mpoint, address_street, address_number, address_city, address_country, spot_type, is_accepted, phone_number, email, www, facebook, dogs_allowed, friendly_rate) FROM stdin;
7	Starbucks	52.24246	20.99455	0101000020E61000009F3C2CD49AFE3440494BE5ED081F4A40	Solidarności	82	Warszawa	Polska	1	f	71 386 19 93				t	5.00
10	Cafe Próżna	52.23641	21.00466	0101000020E61000007099D365310135404339D1AE421E4A40	Próżna	12	Warszawa	Polska	1	f	22 620 32 57	cafeprozna@o2.pl	http://www.cafeprozna.pl/	pages/Cafe-Pr\\u00f3\\u017cna/110777395610257?sk=info	f	\N
2	Bydło i Powidło	52.22675	20.98168	0101000020E6100000252367614FFB34401B2FDD24061D4A40	Kolejowa	47	Warszawa	Polska	2	t	224004844	kontakt@bydloipowidlo.com		bydloipowidlo	t	3.33
4	77 Sushi	52.23013	20.99330	0101000020E6100000E71DA7E848FE34400CEA5BE6741D4A40	Sienna	83	Warszawa	Polska	7	t	228901811	office@sushi77.com	http://www.sushi77.com/	77sushi	f	1.00
18	Jeffs	52.21104	20.98848	0101000020E610000005C078060DFD3440EC12D55B031B4A40	Żwirki i Wigóry	32	Warszawa	Polska	2	t	22 825 16 50				f	1.00
9	Pardon to tu	52.23626	21.00269	0101000020E6100000B806B64AB00035402EAD86C43D1E4A40	Pl. Grzybowski	12/16	Warszawa	Polska	1	t	513191641		http://www.pardontotu.pl/	pardontotu	t	5.00
12	Cafe Oliv	52.52438	13.40885	0101000020E61000006FF085C954D12A40975643E21E434A40	M\\u00fcnzstra\\u00dfe	8	Berlin	Germany	1	f	30 89206540	\N	\N	\N	\N	\N
14	Szwejk	52.22145	21.01640	0101000020E610000087A757CA320435407FD93D79581C4A40	Plac Konstytucji	1	Warszawa	Polska	2	t	22 339 17 10	\N	\N	\N	t	3.67
15	Charlotte. Chleb i Wino	52.21993	21.01874	0101000020E610000086200725CC04354063B48EAA261C4A40	Wyzwolenia	18	Warszawa	Polska	1	t	22 628 44 59	info@bistrocharlotte.pl	http://www.bistrocharlotte.com/	bistrocharlotte	\N	\N
17	Mood Cafe Trattoria	52.19627	21.01391	0101000020E61000005D16139B8F033540CC9717601F194A40	Aleja Niepodległości	80	Warszawa	Polska	2	t	221234567				t	5.00
8	Mucha nie siada	52.25442	21.04507	0101000020E6100000DD0720B5890B354063B9A5D590204A40	Ząbkowska	38	Warszawa	Polska	1	f	501 620 669	info@cafemucha.pl	http://cafemucha.pl/	mucha-nie-siada/108029752573860?sk=info	t	5.00
3	Hard Rock Cafe Warsaw	52.23015	21.00242	0101000020E610000038DBDC989E0035405396218E751D4A40	Złota	59	Warszawa	Polska	2	t	222220700	ococho@hardrockcafe.pl	http://www.hardrock.com/cafes/warsaw/	hardrockcafewarsaw	f	2.00
19	Drukarnia Jazz Club	50.04608	19.94929	0101000020E61000007B6B60AB04F33340F67F0EF3E5054940	Nadwiślańska	1	Kraków	Polska	1	t	12 656 65 60	drukarnia@drukarniaclub.pl	http://www.drukarniaclub.pl/	DrukarniaJazzClub	t	5.00
16	Pasta i Basta	52.20164	21.02219	0101000020E6100000594C6C3EAE05354060C8EA56CF194A40	Odolańska	5	Warszawa	Polska	2	f	22 849 40 75	mokotow@pastaipasta.pl	http://www.pastaipasta.pl/	pastaibasta	f	\N
5	Cafe Kulturalna	52.23177	21.00662	0101000020E6100000E17F2BD9B1013540D218ADA3AA1D4A40	Plac Defilad	1	Warszawa	Polska	1	t	22 656 62 81	justyna@kulturalna.pl	http://www.kulturalna.pl/	CafeKulturalna	t	3.00
6	Kafka	52.23959	21.02276	0101000020E61000002FA86F99D30535406D3997E2AA1E4A40	Oboźna	3	Warszawa	Polska	1	t	22 826 08 22	kafka@kafka.com.pl	http://www.kawiarnia-kafka.pl/	Kawiarnia.Kafka	t	5.00
\.


--
-- Name: demo_spot_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_spot_id_seq', 19, true);


--
-- Data for Name: demo_usersspotslist; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY demo_usersspotslist (id, data_added, spot_id, user_id, role) FROM stdin;
\.


--
-- Name: demo_usersspotslist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('demo_usersspotslist_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dogspot
--

SELECT pg_catalog.setval('django_content_type_id_seq', 3, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: dogspot
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
0mtbxhl28xepl2ty6awanz9stdlzzyee	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 03:36:24.71731+00
mw3lt969jna8luk6sg28pegsqmiy5tly	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 04:46:04.066215+00
d1xsv3v4zip5x5561osphjhwu3bs3va2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:20:24.352828+00
h0gwff2mbjt1txbnss25kktkcao4dl2q	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:20:24.61371+00
b48kl7q3gmubu3ytwum2yn85j5cadnsr	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:30:19.699413+00
n28ohanrfo8wi8w1hh5py28kzhywm5z3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:31:11.183393+00
a6acj2ra5tfzydirnw6wkhp7r21gnxp1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:32:08.032085+00
n802n9xd86gg4v16twkci0ydt31y1bkl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:33:11.972279+00
6m926rcyi6z9quvqsqts5g27k1kr84h0	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:34:26.593094+00
9pk8fr4kqfnugpnlr7wqgz7czd53qsc1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:36:31.323022+00
5et8yur6n452xt1312porm1l6h0a5djn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 06:39:37.90424+00
tpfqpyaz0qv9m10d8mag2h0gmquknx5z	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 07:10:59.321108+00
8aaoh85f1etia5x52eya6nzozldgh361	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 08:15:32.847268+00
2j538otabznyef28ue9nrjp3d9eqkhc1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 11:10:54.535799+00
kldi1jslvifpbhhy9aw81zz6lfr9ud7t	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 15:05:30.036925+00
ygdc77vlbdb5c4y1e9ee6peefzedauui	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 15:05:30.313328+00
tb2ibyy5ef1tkp7gehdxk2gonsyncjp7	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-16 17:25:11.152362+00
cqd7f5x3kj3dpvki9ufwm90o7vulcigw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 18:01:30.850744+00
lp9qkkzyijims9hftt9hjl1wx2wzhw1t	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 18:20:00.851404+00
qp01i6o5sxvceib5d7azdm1r6eotxm9i	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 18:20:04.292846+00
29hzpq7ycu7fulw4luecpa2ziq1vtvsm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 18:33:36.024283+00
ix324f27z4kfyriw94welklwh3lpzqux	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 22:17:52.283294+00
o35ykr78kw2jxkcgij6gfzaq4uuckufa	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 23:02:46.343846+00
kkui50so490maydiqxecxyhzb3fvrwym	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-16 23:56:58.689081+00
xykf2gydg59th3stgu4616cd1gvx8uju	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 00:00:58.771114+00
kzd4bfe85ogja1l2ysy12s049munyrq7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 00:19:58.319981+00
gsmdxroa0y7uam3mjyf62lyoy6v7z2ca	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 03:00:20.460628+00
dkktnto6h5gb6z7o205fz8fx2l551psf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 05:52:50.980503+00
gfpo2y3lrsxk3ne7ughy1h87jo2unsvv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 05:52:51.265211+00
dtx8005larry45tm45b2o5mhnwqztp5u	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 06:51:16.260244+00
91xyn6jyvofq7rtbw2iztq59zp5e9zrz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 07:50:26.793627+00
ywhcyi0dqhiizlzggkd7xmaf8fhgk3hw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 09:04:24.149026+00
tt9o7itheg6siy7oexsdncoeop88uet8	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 09:08:14.033751+00
esda4wr7ybk91zc7pu1jqzndlqbrp55i	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 09:35:58.609245+00
e5qejw4h4ib0brv9h1p16rmgps57ukw7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 11:33:43.227226+00
aonj519ybmiynsexj6wqzhgwg9godep3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 11:33:44.010532+00
funrocdih19dyd5r5f0qjsxuydhl9pzl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 11:45:58.660111+00
th2btfd4yl31vos8ogbkbqpzcykq1adu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 13:20:24.747674+00
c3zojb2erepe36rledulvtlk518e9j34	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 13:20:25.620506+00
de5k2hobw6ugi3tee1v4g2fobfvpwdcu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 15:39:33.165919+00
imqx7vsxsqpinkomwf8nu8y1x66fufho	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-17 17:05:26.362996+00
dwi9tn8ifv1km8krqsl8jcghz7lk6xte	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 02:44:51.302609+00
rmnvgo6tyyka0dwz68rje4ghwx1k1bfg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 02:44:51.844994+00
v8xv4ts5rltgbyqi1alw5tw8xzifwyh2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 02:44:51.901811+00
mv26akkf9xguqbtbukl10m49eptik8kj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 02:44:51.965424+00
xjtw66epw3u0l3b93vk7a48bip3kra0e	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 02:44:52.566695+00
088a10qdr112awnn8tpoqalaoptrlph7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 02:45:17.781546+00
9ouo41oa25h29n11lgl64zinjkp0i0a1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 04:28:56.818204+00
5npw2r8tjwf2doqipejnr7q6y37dv0iw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 04:28:56.944061+00
zi717885mwh3h3we69vedkpq9l48x8pk	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:02:12.363+00
c6qiswf2c9yml422zyrv0txcrbj0jlg6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:02:12.76362+00
1xx0cbd7lib7k81u2p2nj0qloz7u2vgb	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:02:13.675001+00
9axoa4g7nbkba5ux4hfdzsurvilkkm42	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:02:14.580119+00
0buxrbok8r4ezkhktzpp0vvqrcdjwla4	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:02:17.26292+00
hhi8es8wpth3pzyvmh7f9sgpdbuuognq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:02:20.005766+00
htpgkedw7m9js273i3bswfx6ne2p94h2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:02:22.516079+00
c4i92fbv5eb0z2tv16bszbwgbs9n91yn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:02:25.861534+00
02uuf64btf47iu5wce7wkp8b519s894j	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:07:24.138353+00
l09ntxvp4b2pj4a6h038ambylffprofp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 05:25:50.925742+00
vnhrwjicskt6578k64b5d5japy0jp3ir	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 09:10:49.730181+00
l5me3rb05thhncvjxrufjm5m04anna57	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 09:15:55.755114+00
0o5ti0e3ghqkdgslkzy3cb2ofkh1howh	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 09:17:19.441152+00
fbdcxlieauysj6drirvbywj22xwvs2cz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 13:11:02.246792+00
j130lg780wuzc8f4y2jjjz3821qh6t6m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 13:11:02.474455+00
78m51abg878fcx8mnokwe6460ogcz4nv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 14:50:57.158602+00
wv4a2qest039zkh34goq9dsluc83cp82	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 22:09:04.666232+00
lyr2x8fnx34ipv3e1mvz9rqn7d85qreq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 22:14:13.34297+00
s17y7nubh4ddfe2cqfe1aah5ifh84wee	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-18 23:34:22.377973+00
8b7wk4l1y70amelhazqnar28aactwfxx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 02:27:51.147869+00
loir46006ipm5z2hmdmji86bko31i5a1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 02:27:51.373842+00
ymyjqadfg7sb4wqgumrek2xulnwpwhan	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 04:53:42.379893+00
f6j7uc1g5q51umbdbgmjd9vssbgvb88i	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 06:20:25.379955+00
ye1w51rqula751fryp0wft4s2bgegq4n	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 08:30:20.436021+00
qwjzsleostoxusevhqd9osl9xj293nxd	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 11:21:21.793402+00
ecvjulbiyb8b7c9m2n1wolub3ytru4wp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 13:49:25.204988+00
rrbzviuhjyd1jvyd5oqz1oc38f40ku6d	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 19:11:32.8046+00
147nfrx11622udszj3nspacjiz8pv88o	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 19:23:32.851461+00
m70544v4w53ztpdug7cv68zdzf42zsrv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 19:24:44.490613+00
9vxq6m262tv34gfuciccxesnm4ejwagh	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-19 19:24:44.517283+00
1re40so5j4lqfcn0vg8jl7an0lx8c616	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-19 19:25:54.507692+00
aix2qunpya9a5n29uoa7ozdsbe6xomjv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 19:26:00.568509+00
t1ls81k59gu72jwwh3zb7w6ix63ljn2n	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 19:26:42.014092+00
359itmc17sawn8s9hragrf8xh5a4hj2f	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:20:27.587618+00
8kuwy9ytv2e50l6lm6w6hnb3vo3aehuw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:29:33.281031+00
x3sblh70g7lwu1iz8smu44t7nwybjqhp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:32:30.898759+00
axowr469eazss4jiqp0dg951bth16vo5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:33:02.715937+00
pno3y8kb3ct66fae0kf76pun8bhmbenl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:35:50.022412+00
smggfnvk0xfu22ne6e1ywpdanfegr98q	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:36:03.529915+00
iyzmph04zff7macnh16q2jt6g209eo5z	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:38:21.598537+00
t3h4jerymwtt3hyqsylcscr4qftyi63g	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:38:24.269569+00
x40cpijhfxnsp5gjx3ukh7fahqvpbx3j	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:42:27.095108+00
fllcb8eh1cr6tzqnfr3kvj7rt77pfh9w	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:44:33.801277+00
cwtqheflpbxer46w7ez5r1rp8fqw770v	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:44:35.834301+00
g612hrxh8wzbdz28gvaksbhi5q7wm883	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-19 20:53:50.004382+00
txxy5dvmzvy61y51i9wyia7ier6sxg2b	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-20 00:20:10.567748+00
p7ervgwraqgey467myhzveyvk2ry9wla	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-20 00:23:28.722064+00
pybt4v82859s6j3o2068jqa9njl9s0fk	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-20 00:23:40.900617+00
5rdh9hkzkssn0uukm5ogkyjbtidetqyy	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-20 00:23:40.926426+00
wkqh5dukzhuvwjn0iscnontm9ie3wd01	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-20 09:30:39.359129+00
rrbwucdicy8v5kndp2cqfj5ofsiwjoyb	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-20 09:38:39.462435+00
m2x50ijujxjol3ut6c23g5iq18xt2f6n	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-20 13:46:14.101586+00
8cfpwkt8ibk0nggy36onzt0ge0ntllnw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-21 09:57:12.939152+00
zyl3ah18872jijlk2y7h6niwja4g2kwo	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-21 18:48:36.307497+00
eio3asjrsaycnc7j86bnmb4mhwls6cj1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-21 23:49:31.246759+00
tdsb9ek6jxczwtixldwz95ultvqjhf8h	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-22 09:45:18.837657+00
agudubqsqi73gfqide8q6u268yh9kadi	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-22 09:45:21.952531+00
340xo3qfwayuamp0la7jf8he6rr9fvnn	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-22 12:39:40.81673+00
z2ysykoytsudqxi13xak1dykn9mk3hvf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-23 07:21:42.843361+00
nr50v3e9ntsnuum3ty7t9ctbvgq0l6cv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-23 07:21:43.761911+00
5ru6hnx3t3qpb80fxjuwxk3ajvzeb4zo	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-23 08:21:40.062154+00
43fyqiadtssnjkrdtaulfzywms4b285w	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-23 10:44:04.105318+00
rmm4t38j12jrqw0isznpxz5rb3pdugs0	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-24 19:00:53.528684+00
ajmv4e81u1tjy0pzbcjenf059e8wgmez	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-24 19:00:58.421344+00
l3liapzs8d6gh0zzp0st276t7lwga4b8	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-25 18:27:03.260389+00
i89faigxec3v9oyeuqvklnd1b4xidh3s	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-25 20:41:34.568559+00
q7lkirp1q690mdh186mqkb1dtcarrquo	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-25 20:41:34.737679+00
ovahptewjx03nlczrfgcok4k6u4ysqgx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-26 09:51:52.816579+00
xiquq1hofpwymrn8qrwrrrmgqlhgcqjy	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-26 14:07:58.534344+00
g9mphwebof8qoroays1cxfsl2ep59n2n	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-26 14:50:57.266019+00
hf6xe1r2uefu8fuw6pt30on4p88xgknv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-26 14:50:57.479549+00
8uuhixack2trwxic0fhv88xgik98tpmn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-26 21:18:51.946783+00
7proo50e8bxxy6soimcx8ut20p8fd27c	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-26 21:18:57.872593+00
e2z6u9l535uwvpgephweby37ie12e7az	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 01:02:20.129878+00
iqtromm07ejnhexzd9ynxalaiqws6xaq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 01:02:20.305423+00
s40td66rbnt2d3z0dqx8xo6c9dllyiud	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 03:01:43.804026+00
sl0y0szs4rjsvuhmrawugc4yrtvyvlch	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 03:45:50.023087+00
dzdbxio5r1e35ks0jpyhqgqxunkz4e6j	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 06:51:03.447514+00
2ytyihw00jekm9c48uv9vqp206q7cdut	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 09:49:34.391059+00
2sia3uk645h9pwm2rd6ldlr5oirqy772	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 13:41:08.533164+00
ptj6fcqnaiiy9elblxfsjmyp72h72tir	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 13:41:08.796998+00
yzykvl8ol2ei7i6vmubml5r0yd4kxjzg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 14:57:13.167499+00
e081nwju0f6gv7lqzal4vpo2vxhyktmu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 18:04:19.497999+00
9i3sheq3qfeyubhdmgrfti0x7kodr5fw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 18:11:22.333831+00
11g8ilbyq5b3h1chslwp70hin1vstltu	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-27 19:05:21.74489+00
ktrr293mgc32zkmx9636eyiz8js8djrk	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 22:21:44.651828+00
ssltbtn43g657dh32gmbcmyiahg8kxgd	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 22:21:54.559336+00
xny0e4qzrl987zwtgpbuf0gcxj33sqth	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-27 22:21:54.80177+00
do7dujjm36h2jxla0r7q9va2f06w98sl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-28 23:50:06.378659+00
kiu0qr1buig0i7raz098uuah5spa4e2m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-28 23:50:06.532905+00
ujw2n550sjd47xij9cgwks1g44k9vaq5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-29 02:49:28.900118+00
hi6npup9qhqit2e5rdv7ovw8f51millm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-29 05:45:22.56182+00
818gfrenry4ysajmcasojjkrbw6digrx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-29 08:42:45.117766+00
ilybxqc1xoeeiw70cp3x4hjk4ikesglp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-29 13:41:01.178186+00
nc6wv3gjivmcv13lnqjiapmavewxmar9	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-29 13:41:08.53576+00
gkmw0gsnbczpovhaigmg5hagh37ckhxh	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 11:49:17.523682+00
8j3lz6rd7gihxykgc3xvcvc7f88y1jke	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-29 18:55:31.920331+00
iwlv1tr5kklrv2r0vxr1r235w2gx4d3z	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-29 20:00:27.420832+00
l4kqf1gdicg5c7xfe5lymyhwdh5l21r1	NmQ4ZGQxNjgwYzcxODBkZTAxMzlmMzcwMjk1YzczNjZjMGI0OGI0NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiZGphbmdvX2xhbmd1YWdlIjoicGwiLCJfYXV0aF91c2VyX2lkIjo5fQ==	2014-09-30 08:45:23.225494+00
fxhx6z3qrlp0hxjxcm6hz1wrqcf2czwu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-30 09:27:31.286569+00
ybeoitl8oif5p1mkd04tq7jm9ncnfo4b	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-30 09:27:39.562056+00
xxbpe101flfuznndz9cy19azbi5i6em6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-30 12:00:08.17832+00
8u0h16h7wuds2uwojoxcuetix4t2mh7z	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-30 17:09:10.044119+00
mxszii9knyjwe5azpwpbamni0wtggvuj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-09-30 17:09:10.272774+00
x6jdsqeqpifjxx76lsp6xhus8mvndznv	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-04 14:14:10.633806+00
jpbbb61z76bl04n9252onp1844fc96vt	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-30 22:09:03.624284+00
80xma8yv24rvsr4gh3p85vzgbgdjkywj	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-09-30 22:28:22.383104+00
ttsb8sl3dqsfhf6us19sg1j1i72r5did	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-01 06:10:47.185963+00
qwjhaxy24eh9v0gxoq8gleo8q0lt4pkb	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-01 07:09:13.590026+00
kack59qs92oqtc3oa7x1alifqmjvj9bb	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-01 10:49:28.501087+00
yr0rgc7rd1f1697nr2osohbtguaoowak	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-01 14:19:59.285483+00
g7akziuexj94037av74730z6whbuftz2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-01 17:16:39.214507+00
5wdmabcdg9vxjdkj9n1hqf2dg1ngjdc0	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-01 17:29:33.988047+00
1sunad6eq5h4qmzbvz8z3ohoef7w191l	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-01 19:29:37.059947+00
13zuszvusktkltfb6r7vjj7i4bcz1bzr	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-01 22:18:43.032916+00
9t8htu4a7zyqvtt23bvhsqm04y18lakt	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-01 22:18:43.38317+00
j17zmf3j33lm02vq9jnr04kvkv50e6e2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-01 23:16:33.524927+00
qy4z0fthzh2hpojexvf6j1yqmkmomrgy	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-02 00:14:53.136157+00
flopyd31iqxl5xjoj7md2zcw0jjtpbmf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-02 03:11:58.997919+00
obq5j4b8nigm8071dyjr5smbslzo238x	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-02 07:07:28.582399+00
c0qhlmdw5e9povjxuvb2pikt2s37pa96	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-02 11:51:54.527424+00
kz3blpfjhkohmtisoyman12cmueior3z	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-02 12:03:13.217745+00
uvq0yrq7hdshdsw1a06xumdk8vcn5d0c	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-02 12:21:45.057568+00
27blbt9tvki6ybjswtbh4klwmzsl4mid	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-02 16:43:11.308972+00
uexko42c7dqy2ssz2b32npfihdx5wdf1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-03 00:34:23.458876+00
lc6usgcksrm79wg7fqtz9l1kz4g5p868	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-03 00:34:23.645143+00
9r6782rsjok42epfamyb7pj39hivtolg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-03 15:58:07.163271+00
bkra33r63mmsgy0wnblp9rl894tw957h	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-03 15:58:07.370214+00
wrt894hp2scpw8bzk5jqeo8492eoauku	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-03 15:58:07.579459+00
t8pkeiejlf9ni2wunad4yeoyizvmz54v	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-03 15:58:07.80895+00
k8d9j4huig369l51a14eohgsvqvfczf7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-03 18:05:06.983378+00
jcgoyx32v45cjrfif1sz7dv8sfkdqnzi	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 06:49:49.310689+00
hefin882qnl70k7w4j802ai2ew59wjuv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 10:21:52.376238+00
pla1bc3y7lrsfe7lr5m7ooj4rne75lz5	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-04 14:14:13.857373+00
mim6meukosbv5ijd7ac61tt11galxdjr	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-04 14:14:17.8206+00
6vsloz9unyf9oiyuk40qj8u6qxe4g63k	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-04 14:14:25.199332+00
oi9uecusas5r8yib28yk5ccxmswej3ry	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 14:55:45.508235+00
5c7gtc0v4m37rzvtccpmefk13a57zpv8	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 16:00:46.272392+00
28ozuaq2mmmswyacvg42pilfmfdzph8a	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 16:00:46.435641+00
7mtbpbeldbyc2e88x01ultjrfl10w9l9	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 19:51:15.628889+00
gaz590rzkozgncb6egqdh7v0x4jy3vwx	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-04 20:23:28.701278+00
fqyub3zty36fagzc8ivccm490e0iajry	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 20:38:58.996459+00
tmzhroay2um841f6s5lr3n758hml7z5t	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-04 23:46:29.332401+00
tjl889hjg4u71tjfasf4wfyveb6osjvs	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-05 09:13:48.574966+00
w11jnb6hn27cp98ej2yx83mgno82b9sb	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-06 09:18:47.561541+00
p4r612s6meudqwzp9ubijpkyl566rka7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-06 10:08:14.830478+00
x4fovxt952td84s72w0aromcj6y3xw8m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-06 15:42:50.575366+00
twkt8igvqe5hvseyepf3n7bfjzb448nq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-06 15:43:07.85428+00
8sckzs0os46hmkdqim70ttorpnrmtqnh	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-06 16:07:16.673499+00
3f5w6gr5ecl1l2zbgytl7192wh4fv69u	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-07 04:56:18.662359+00
svvgxhcv34o3aerqxum8rb23ae6ii7vw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-07 10:17:32.500904+00
c8or29kpwlg78tmg90j8vkfx5y30hojs	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-07 15:12:55.420406+00
c5ruirtk0kp5nfe91b9dcpw82obvhv3m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-07 15:12:58.057891+00
jfsmb3oyik4nflbfiv36rfxhpr7lehq9	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-07 15:47:19.907923+00
snmzeshl89acm8fddr33uu65x7sirnc5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-07 21:19:19.908256+00
uej0keqttsz23ccd30o7br3zbevudqp3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 02:44:19.170512+00
m7gp563i6faygnkhlorub46lifwre6t4	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 02:50:08.15472+00
5clvl0y25p26s13d9uhg45oimzqsq5xl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 04:39:41.658963+00
5tg2r4y6sh9q819wznh03xlc16g9ugk0	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 04:39:43.592505+00
x8urb8hicnbgl0l0p7ka0ficvgoe60eq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 07:41:47.292375+00
3zvgx6pzf5aio7kchl4errdo3uctmch2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 11:10:14.346138+00
bzrx93cn9j3tj5y8ojlriw0zgl900btc	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-08 11:11:27.077887+00
sszbq2voyfxjav8jr7x91a2uwi359pka	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 14:15:37.103124+00
kqhta0i8vq932v94yd9lmyo9yo9k8t6l	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 14:54:02.945951+00
junsdd303er55fkc3q0l7rjgel38hql3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 15:07:27.230369+00
3hptbq213djgd7tfly695hmnumouayf8	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 17:25:41.848784+00
rf8p4pkrpz7ka6bg3ukcwc2470g933jf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 17:25:44.222692+00
izuk49wkfpyj6h24qarfa7jal7sjvl13	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 19:36:54.945638+00
80bk796273ww7lfdfirfuzz3l9cvauzn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-08 19:43:04.503904+00
9gr854xqi0hg96rygefbvx5uh9mflq65	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-09 00:20:29.442578+00
9bk6rkxu5278ef8qdaqgo0wr1e4kft91	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-09 05:21:23.268008+00
s0k52k1wis6cm5nfha5vphbcce5xrglu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-09 09:21:46.940693+00
lfq4wj30bjmjw4sbn4n4njc8o5izqage	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-09 18:27:30.011817+00
vgliwgphmrplh2gikzzmazgur3e00obc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-09 23:51:01.927831+00
ihr4j87kwb4x42gdqlqw9r8ez1llvjpw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-09 23:51:02.107595+00
7kturydz6som5zkrek78kxq8zx97r08g	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-10 02:59:41.475066+00
bjewnbcoky599rtrn4zyhcg7ijfu06jl	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-10 09:39:33.123192+00
18pxtinn8ghrdcxru6bbliub12ywcyoj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-10 12:37:28.820686+00
by4kkg2amp7pz6uybviyvriffvy0uexo	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-10 13:50:53.450633+00
3zurghpjr61bc8jrvii2404kopgbqlrv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-10 14:27:41.8529+00
u3u2s17cmjijhktol8qol7pebbnzritx	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-10 17:45:53.388285+00
8p506er7yxfvfya8wdv5k5bgmc0lzeyw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-10 22:03:49.231611+00
h73e0jwqh6po2vsewmktoqh5d6efxb73	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-10 23:58:07.017463+00
p3wo0mrzjhpp8hqikjzh1r5q5meddbmm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-11 16:31:54.132179+00
4dik6yyx8qongldhfcgiatbmg9mt3mik	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-11 17:00:11.738586+00
tuczkt9jas8xuzwxs4zapnphkl3wr76i	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-11 17:47:13.676495+00
xl5jv4pwzod9hnqq4eli8y71e4ijs1ga	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-11 19:51:02.473671+00
mczzj9aafvht095vfvxrw4wccp64i4um	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-11 22:19:09.515709+00
a6xm10y2zd6xbn6blwn3zgzweyyn11xh	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 01:53:38.992855+00
zs8elw9fi5tkthe0wm2601voj9u3jfi6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 01:53:39.218446+00
v877x20n6o8iyd8wj0ftzmuhnrp91ora	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 02:03:25.695941+00
tp4dih1s7v2u07rmdplddf12zv2rm512	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 12:44:57.700663+00
dqzgi3blagdtsebj1nsvupihuotiyygg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 12:45:02.968426+00
45ouole263ofahwa1lso371mhynmsiq5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 14:59:29.876264+00
b2627sj6fr2doy7l4g8o915vk2ri2dqc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 19:48:12.201798+00
68xv3efx9bmadjmhgqoyqzfqzx7lvg7r	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 19:48:12.366032+00
o7c5x4ergwlbrlqc1e6njl8le1tw17fl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-12 23:42:10.969238+00
4vk42h94rt9uzyo7z3tfney3l4aovle5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-13 03:36:20.817073+00
kcd50d75dl0kmhbbo46s815dzjlthj5u	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-13 09:50:34.899806+00
ogloutlhf2pubpgks8jvdpfrja0s7bt5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-14 10:34:51.582777+00
ayvqbp41r01wj2f8hukm7ubvacqed8ky	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-14 10:34:53.872351+00
jo6xsubs59kpecoh05c98ogbn0md12z4	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-14 11:16:54.120685+00
yrjy2jbci1al5luhd8ykdpa3xy4fegkx	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-14 11:17:14.364746+00
umvhg7fcxktcsdxk4cm082xz3ke3t5z1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-14 17:28:39.22755+00
273227ycd8iq5iscrvmk7jfx5dipx3j7	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-14 22:10:17.825282+00
zr9cw7shco6y2x3z091ett6bz87v6anz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-15 06:21:26.550433+00
lknq0828qlk76dgov0qx9ttyzqi6hh4i	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-15 10:31:25.696321+00
d80dpvtt3tyg3te49kn2r2cgxz1nq9t4	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-16 10:10:32.321807+00
tdo16iua0npbtb528jjb0wd5nznrbb5l	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-16 21:11:28.155557+00
bw152v7yzdlbxxcuoiev9z3emgxw1jxu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-17 03:53:41.396591+00
b2ujz8jpq69oub7zrs0a318cuq1wpsoq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-17 03:53:41.576757+00
7fe6mq08ahk6cf8r420u6e06qoosk37m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-17 13:49:50.149007+00
8q08kqv7vyeooyrxag96lyk4wn8avzdz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-17 13:49:52.362151+00
cna91n186ooaxi1f4n03oipkv20ss7b1	YjlmN2NhMDcyNGYyMDUzZTgzNzNkNWY5MWY0ZGI3NzI4YmU5MWEzODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiZGphbmdvX2xhbmd1YWdlIjoicGwiLCJfYXV0aF91c2VyX2lkIjoxMn0=	2014-10-17 18:01:24.466625+00
sbonbwdra8rn39ibg6f8if3u2wym64pk	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-17 22:20:00.181001+00
ogthnwv718lb77rqp36ojfr27l2yggz2	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-17 22:24:34.749584+00
5xni4jgcb91zzbgowbdioeyhlwclgp9d	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-18 03:37:41.460028+00
x2av2b08wq4ga7y19u871aoqy31mgfkd	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-18 09:27:48.713344+00
iem4n26725eex9yaf2ecr3knaz1oqb12	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-18 09:27:50.995825+00
t8n4s5lo1b1pjjz9phwoc0tzi40kq9ev	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-18 12:04:56.385614+00
wepn9p257kthc351r42m5bz2rh55k194	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-18 12:04:56.561858+00
vh2702c8a9qhxrficqpcibl5utis7c9s	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-19 09:26:36.697576+00
s60tnont6mt3ddof6vabwnf68iwlmi1k	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-19 19:34:54.190278+00
lw62s0afh7wvv2iftjvd33awawal0i6s	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-19 19:34:54.420563+00
ykxca7kfe62ho84o32nd472ia91ldnla	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-19 20:33:02.711284+00
po5jetzgcnq8jtusjw1hi5r3k331rii8	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-19 21:31:18.937301+00
f7vh46vlnl0og0swzw8ykkpsg4ici1vp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-19 23:29:49.580627+00
hvlxmeasiug4xmriwhkz3i7b90ktqz1v	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 00:29:12.875824+00
hhcb6x3p9qr3vet4vzhnilmqswm9pbk4	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 01:29:26.075059+00
c11wrmct7k8rzxasf8p0bkok2esa6llp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 02:28:43.342121+00
41b41wt426tjw0b7i0kjm2iqt9lutxyd	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 03:27:03.287012+00
oah3y3huihh4ndiz06e3ho9t96mfv87g	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 05:21:48.761611+00
aniuy5tpozhxnaxvoqs8hjmzdhahwgep	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 05:23:41.624723+00
gjxg2v2ei8zsfier5x8t9v9cuw2po4dw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 07:20:39.778423+00
sym2s1ueevoalhk3zss07ghiio71rh4b	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 08:20:22.463926+00
oaezznq6evk2z7iahic9x5st2chh5j1t	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 08:20:22.591394+00
towtoaqvz9clgvr6invlv2x30qn5qbtl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 09:07:23.901543+00
h30t0b23jj9hmafzs27i3q6dmw7vkqvr	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 09:07:31.387807+00
qv3t1lc56nb99f1r17ojzju5lh63dedg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 10:19:03.220361+00
umt90mkckfhge7dri89ebyba6nvcz6q6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 11:16:02.333103+00
9rc0bmvsqh8aehq9x8wl08p9sb614v96	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 12:14:13.280879+00
oce984ljxou73nwg1mldvvz535i19pcv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 14:08:58.879691+00
sumos0ypqonsxwvv70oq38wiqftil8mj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 14:08:59.057588+00
9c1ildghaijlp1w0z7eld5eogvjhueyx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 14:51:35.362318+00
fealwy0jo5mudsewfuuepd3cxw7hnduf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 14:54:00.650773+00
zik0igyu5mmplpvcrka18u45i3fv1lbo	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 16:07:23.746262+00
8ldrsddq0tomz5pos2w62i1p2pfhrzrl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 17:16:15.140425+00
5z7v0t30cvcga9tt7885nqov4n4wago5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 18:20:00.205277+00
4ga474a3a9zewg0nv63rd61v8ejs3nz1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-20 19:24:39.804184+00
589gflzavd02ngnadks4j06thgcleu5m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 07:47:13.289316+00
kx2pd8nxxc64sz2i4n684g6wiaebrr6g	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 07:47:13.448506+00
afrz658n9d2b05ki1j14997n87pq0arn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 08:46:07.383388+00
olq1f50zd0hmrjt7d46ffnl7cl1umxri	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 10:37:42.437157+00
xz2gymvbu992f7t62rj59n5a10utpc6e	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 10:37:47.307535+00
04nf385ru76mj1nsognnftg3jpru3s3t	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-21 11:44:55.701469+00
9zju9anbjd8jyifjg6lcv92mc90v0rdj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 11:52:52.95943+00
n7olfnz2kxtlh8klp0g6jmxkz1f1tyer	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 12:36:34.019865+00
dibqegpb1ef6z5vv8qc4c6qxr6bbbi71	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 12:36:34.278714+00
5tvg1rfj5oftdstnnjztlv2l2q2qu708	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 15:45:42.755576+00
wdp6i9v9269nqbld5y255ii2i9c731ed	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-21 16:31:38.894996+00
q6lj0030lfu03otnnw9vgy1uk2edzmp6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-22 10:42:05.621526+00
shs35gs7cnepehzw5fagblq1y1x2bkkx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-23 15:18:10.506185+00
udqp8gaiekxo7lqu30d4vyl14evscbeh	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-23 23:29:23.715369+00
8gtz9zcwtdcw53399qprd39eutty8ngz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-24 05:12:20.687954+00
y34etuoabahmxo3rubd457k1m7lknd1l	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-24 05:12:21.030162+00
t0x5makbvkp9ic5r0hdehmf89vznbv4j	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-24 10:36:49.130539+00
6tepijcbf75qhyftd4o61ezlv0nqr2fr	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 01:45:56.560688+00
iw8lapvhpxaf3vzshw5tnpo3j3jzv9kt	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 02:45:06.392105+00
m9l211wyxh3d6iphphw0ceixroe0r6cq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 09:56:54.848222+00
iwq8vrzwa09nrtyv49fk3qvgcd96n11p	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 12:20:15.840986+00
a5kihvn6wquic4rg2npza2usckw1z5em	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 12:43:10.216856+00
hs2yr0ozi8xvjo8jknt9mqbd611nme4l	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 12:48:11.393397+00
bvpf3xjofhvk8ghietua5udo6byfifg3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 12:51:27.751217+00
6g8h2ehic9h2zjdoenzw0zkclnqgbsy7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 12:59:05.790303+00
jlo5f9a1qsp6fs6d3bml7zw5kc0awptm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 18:47:02.443655+00
ilbw9z4f0hm1rn5khpdst7jkx4j563tz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 18:47:16.245703+00
a51glmiz1le46qpbq3qygqkwo5h8yrap	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 18:57:56.234123+00
gfic6d06eo6m8wgeip9hy3cumjsdk0j1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 18:57:58.486206+00
vy121tbaiv3l8ecgj1ip4wokfe0duosn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 19:35:19.858973+00
tynkjwjv8ndkmpwleit9n08qpxypzgv2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:12:41.225357+00
5yqhj6ubqu7njvt8k018o7akfdojq67l	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:12:47.716982+00
cqyougd5esk9502mu2871rtvgigyf153	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:13:19.453769+00
51d3lr94wjhcq69crrs2h60bqdchjxxg	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-25 20:13:19.481575+00
jb83icaqyh2v6ovkbu71x9z16ge8wh0h	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:13:23.95116+00
ya3hztlbrik8lqt3g7db7dmhuneu56pv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:13:48.725604+00
fxdbidu27c0505smx8ms55xyz9y790mx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:13:53.666866+00
2s3o610u6ut0bipzdmp25ictukiehfx5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:14:57.659411+00
tgr2ficm0mxcz64ctdyjocwhri9dxdlg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:15:04.304966+00
wstb8gehkai1c6eooioitpn4tnvhdmr7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:16:24.647427+00
ffoqu4v0a2jkxu147uongqaul93o5s7k	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:23:07.337734+00
aevsi42qkemkanxv29mxhfyi3m7oh1l2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:23:10.963369+00
ghj1y1fltjvom5z9q7ns2smr3azf8z0q	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:23:11.803932+00
rnqp2wa2xj3z7oih1d2il1svffsyzfs1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:23:41.387431+00
a9mzjj4t1ujjyxepcm0roiqvdp6hk9km	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:23:45.662558+00
pxblfvt1vlp09flrlgmqb84tkl4mozn1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:23:46.862593+00
1kiwi836fgzakfkir3ueshteeswoybfu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:23:47.295614+00
at1rat5eb4pk1e174rybu44vy274tp0m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:27:43.477989+00
5us6t24cutl2gpxh2oc8k2rwlbgrydiv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:27:45.847212+00
d5450p32rt4jtws9ecg3k0hqv9suamxo	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:27:46.424162+00
wvlpfbxb8boma08o7iet94eeyvor8x7t	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:28:01.505382+00
newgccp7mopq8vqpbwdoq8931v35l0gd	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:28:02.079405+00
6syt4pjd5icuwsoibvn5pc7eoccm8zor	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:28:02.203098+00
zwap9lz6y5lpaucna6ic16iqfv5z3rq0	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:29:43.525955+00
kq0wjozhzsod46pkuree3sy8newjl9ro	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:32:53.952511+00
h4hp7hw7rws59yw9ozzt5qn03qgt1jdn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:33:17.84785+00
eha771wzjeuoih1a8lz3pgqr1rnqgx48	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:33:20.252988+00
ocgum16mv4gkl3brxyxspab4dyutdh80	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:33:21.514489+00
n2bw7sga12ey6nntsk67j8990csyzudc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:42:24.12494+00
z40x9wuq66bsnkgt8845q1a5nlxa74dw	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:42:27.583961+00
vf2cy3vebgudmtmbc869pzpxe22qacel	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:42:31.792245+00
wln2xgurwabe0vi71zmc2evnex7ukgkv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:45:06.138003+00
m2ihmjz7alci7253379rywo9c793usys	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:45:08.408338+00
yi6anjikkd9vg6ufxb76fmfsx5teb1rk	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:46:30.379503+00
6e8xwduqjh67memxugw1rzld6307bf8z	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:46:32.995509+00
8l301xr4u86gmu9wd83hr2cau7iftjub	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:46:34.595937+00
pstd2zja13zla50k6j9pr94ybne0p4mk	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:46:35.511336+00
1lnj24cgls5j65aymxf7n57ivk3sa7m5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:46:35.857586+00
of7ku68nl684fcus6almk4thtb541jo3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:46:46.086307+00
epbic9h90z027xv87ow2hoek8iezguce	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:47:28.043177+00
qzgrw12afwy4lz379xgy36twstm57ksj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:47:30.285854+00
pm2f4ih5omokgkg2swpvddxq4ltzlnrm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:47:31.493762+00
l78bqwpfd2cz9fxjk8ns09sm50cu365n	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:47:45.855666+00
7fembbb06y8v64i02auhxvwhfbyjiwn6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:48:19.881318+00
oivz7mf8i4ozwjmhdsbe05qmt6fv3ino	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:48:22.244945+00
2t57dxghd2ei386hzsub7z0zngq4pynp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:48:23.568323+00
pyyozp77a2dna846hay7ciuyn3r6p8y9	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:50:33.657638+00
91kw2fegbi1cjq7f70dg35ota52umok7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:50:36.443875+00
pkb3cs7nmyin24x7gmras5g88yhkcerj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:52:54.582138+00
xz0f4r4e6qoay0ya9j47y3eyb5d5xep0	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:52:57.243633+00
3w5u97n2eb04msk3cri519qtmp7zrynm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:54:47.101204+00
1r6yu0lkhpfm94xicfc7brivmlv75lau	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:54:49.89073+00
i7unui73exu9ozra42jn4euesbsa8q9h	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:55:10.401117+00
mswk37gekryhqxre8ylvb03q94kixk6i	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:55:12.92519+00
fwzbm6mflvglog4q64dhcnq4kvmfd59k	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:55:14.120043+00
lu84dn1uze99i2ujlco9xnsciasmv30n	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:56:23.389999+00
rik4kwhewtqt7nodeved80zc2s8vegft	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 20:59:19.384341+00
emt7ehcwagogj05apsny570kkopwhxtl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 21:56:45.372851+00
9mff1y7xlz1lnc3j28ixjp4ts2zmo8oz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 21:58:31.122935+00
bsptd0m3s5qp3ha25z67z97by7jwcw7a	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 21:58:33.575821+00
5g4c9mwfuenkq2fh72mdue6xyq56tj2a	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 21:59:36.607315+00
xjpw8jfcjyz5i05lm5kh95azpfjvgchu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 22:00:08.579876+00
cgmsz05knlj05ho0a3dskemy1w1fkxyn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 22:03:07.461684+00
xfspm1jpwx3kcqek13jeojbpz1v09oxl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 22:25:28.848977+00
no7jzi6at5pa8r7af7a17vd7g4btui8p	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 22:25:57.890247+00
l08pnduw80krfljdjs1pwe0wvj9yi7dn	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 22:26:24.537831+00
ab9stfnmgbkzfqlnc7imb8irsqxj21rc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 22:27:04.331936+00
lrgknd9kt1aahnkpl25tnr2lwvplbb81	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 22:36:09.411645+00
olzovwnkfu8xto4qji27mronzenuu0ol	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 22:43:53.052921+00
4y4vodn4z96so5ba6dwxmhrd4fmj3t8m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 23:05:26.117586+00
h7hoakv0rys0aodfhldxg6j0lihwjpnv	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-25 23:52:03.01785+00
71zi89fnwubl9jz29datfpl94so0sgsy	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 00:07:41.692363+00
8xha9flqnc0dx1v8der6dyhftdhqvl6m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 00:24:10.593324+00
h7r7x9hz8rsu2o35swjbnp94ytqk5l6z	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 00:25:44.670857+00
mut162yd7i73c6p2snokap7q7erv2dht	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 00:25:45.408144+00
wsl5mkj7n4e86xjj00t3ve5f9s6zgkbl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 08:00:14.553152+00
uunjpn53u5p4s0kx6hnugoz61pnb1ipk	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 09:03:18.726634+00
rp7e69bhy96h9def5w0lg4yb6rzjg8fc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 09:50:12.786143+00
egc7he9bq9bpwwle89m84q2z4vxav4c9	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 09:50:47.474917+00
j1wgzopu0zwlcdghpx82gz2eo6cwau8u	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 09:56:20.384765+00
qd6tqflnn095f303u522g06f8pflchuf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 10:04:50.630793+00
nudcvk064u9ou2y0qhwpnl0t92qmb8c8	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 10:38:04.394548+00
jq8ej7qp49cplitpbp3o36bvrltdqmi7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 10:38:11.514059+00
qobkqkw6kbjjsldeek54ib456tw584tl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 11:12:33.959798+00
ntiens5msfu182yswz586top020hjcvf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 11:35:30.710318+00
e4zl1bo6j904fwp516ff52ixg7ktubwy	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 12:00:51.867384+00
pvno3vpw1d18yhd77d8qv8vce5wcihnm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 12:00:54.179008+00
owg5mjnszsz4u7pzkmuqccq9g5ptxf6b	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 13:27:42.729962+00
c74ojp4mkx8poufh7khxejk2bf9o5yeu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 13:30:25.531063+00
qh8pqr1hza12iwcwxwjlhn89cavk4ov7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 13:31:18.695019+00
iihrjigwmm6ozjkunn9al1azd2bwy4it	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 13:32:41.991112+00
ne6xbbzjpsmrslrspbz24omvr504xv0l	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 13:42:55.950135+00
woiscsc1x112a9zdbz1wmq3nxygo5r92	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-26 13:43:22.760022+00
2p195y9b8dhte3220pwmkbp8g2mzoak6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 13:45:13.242916+00
n46i0wsjpfvo4ez590n1nq64qrt35lsr	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 14:01:46.049998+00
sdzqie3gapw1r77bxii9ew99aua5kvrh	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 14:08:28.333724+00
wdht9ozrzxuqoacnhtm7ubl6mvacb7s0	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 14:10:38.086859+00
awdq9mkrrmq97ewe2o5phs69n1ngykj3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 14:10:40.857087+00
9kktdiq6q4tuvdnfzv712vrzittzepay	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 15:01:44.503654+00
uphdpkyjrs5mqp6ewn3pwfnwuul8hnt9	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 15:45:01.193203+00
xue3cadibhk5pl90zhydsiw6jjupl8f4	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-26 15:45:01.649516+00
mmavnzql92xty7acqpuf56ioqwk60ptx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 00:48:24.165396+00
a4elwwp75lgf1vj07sskt93bn7yhoosi	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 08:18:13.848506+00
1sdr67rfce97kb5csqle7crb8jpxcmdl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 10:09:37.124679+00
arkh27x3043issz68r0n92408nem7du5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 12:00:26.339243+00
lhg170dk1wdjideyjf5kzflur9jza9ku	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 12:59:01.623973+00
eynwuj7qyzphivhodlq12plux5q1dnmd	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 12:59:04.294838+00
ydriqdsfbh3lywrqskgfy7y2yuavvjss	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 12:59:06.352413+00
3fy2j94f09wfi4j708ifm8dgm1cgrjms	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 12:59:08.822473+00
t79l5rtn32lfr53wrnb6fnmp1jg9zqvo	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 13:03:23.1528+00
z3n8oszxmn5odmabll7v2lwnqgohrq9s	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 13:03:23.354024+00
wwuy2krf5ab9c0a3eiq1urs0l8hufplz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 13:10:31.897957+00
7qufy70a4pm5zi2s69g6zpq6nb3kqphc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 15:58:56.799487+00
2su6febgwtcgca6bt71yrq33vykoi5jr	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 16:26:32.724295+00
8cqop8t1jihn6k223zn5wroxbsjh7isx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 16:56:10.406428+00
w4o6sxljf13001je81lerj86kx2htzyc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 19:00:04.201919+00
3ywgc2plca2cs2fe3po9ols3w0c4cxvg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 19:00:14.09568+00
d88etlqv0bnitm2hbc4ktumkts9nvc2r	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-27 20:02:33.521751+00
hab8tixwy6uvjesi5t1dl68idenrxps2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-28 06:29:43.645242+00
zbbtjuel4lrbdhmwtjjjy4w7u9n1f70c	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-28 10:02:42.651392+00
cro756pbri4ufnzwqzwt44vbu7a1xiec	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-28 10:02:44.706407+00
kwnx2rm5a2nc10s4dl3otrbzan21iruk	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-28 16:36:46.435456+00
8f649h37jpud8ioraqr0xc9vj6zlrgbk	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-28 16:36:46.466267+00
2mjxchqjojdimcualunpx8d041oe8so4	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-29 10:30:40.407305+00
znopnpjxdrl52qyt0boto4g6vn3zxil3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-29 10:30:52.955845+00
fdqzn0i54ezcx9v8qrroov5g7q6bb9j6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-29 18:37:22.896954+00
jzcszo48h71cjsysv8pxjc6uhjwzv78d	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-10-29 18:37:22.92745+00
12py3x4wt1gqutr4yey534hri8to623g	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-29 18:52:55.78584+00
aj2l1yy9jjboemru1itdyhgsna3xx6se	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-29 18:53:37.211803+00
jyqijshbvqmksei0ncm6973h4gea9hss	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-30 09:33:17.466721+00
h61ehuwhg45hmi0cjj87iww6gb90rnu0	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-30 21:12:40.539405+00
4fn1sfu9r3cxzftlheyzkj5c2amypzqg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-31 06:15:07.275393+00
n41o69yprha9oz92umh31i5ffdm2vqku	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-31 10:32:31.919103+00
oif26ruqnbz6hak9ohaxzn5oc8r3punq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-31 10:32:32.917841+00
54krn7ok93rhez2ageu4f9e1v2jltp8g	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-31 17:34:42.453563+00
bv781mowk56bysfrjj1aejqjkmys7wcd	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-31 17:34:42.721009+00
m955onsyypcgqress5imiubk6ac9n73n	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-31 20:34:11.865251+00
loe0styrdh9vj0m203qk0n2rraimnuzp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-10-31 23:31:09.306092+00
h1lkrgg8tniey8kc4cmj3g3a1zbwvef5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-01 01:19:38.609054+00
ohoqxm181triwuzrawpe2mptdkjl6rts	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-01 03:22:01.630265+00
4jz2ag0emjscywsfkwvvjsvs2uk4qoyq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-01 06:18:28.096322+00
6c7cy2ok5cfb12028asty161u7x394zz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-01 06:18:28.368214+00
j4sua0le50ffirxalk0bek5mpfly2w7n	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-01 09:14:28.5196+00
3ozccw6n9cqron134e4y1mbkwfxqf3vx	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-01 10:11:48.872617+00
dripcb6qhs01msg7z2d9ql5pgbjcelkz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-02 09:24:53.00859+00
eexuv8daum710az22ld0e9zwajbsysf4	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-02 09:24:55.978178+00
c9olzwcgv25o7zbniqwj058aiht40v5i	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-02 19:17:17.982238+00
zz94wpqt0s08nkmsant625j8amqs4x8d	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-02 20:19:04.441997+00
occvlzc998vqpf1cxfmufb2ma6qo8nme	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-02 20:19:04.568029+00
i2dty1fs3rjhv8gwe5hie210adlxkcnp	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-02 20:20:35.46466+00
cqkgdc66youfg663garoyd601loz08cc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-02 23:58:04.702222+00
kx3jcholg92ni7fue2ndd1n3xwqsfb9m	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 07:39:50.309092+00
v87nf92eg6q5nwvvth9qhep39a9pbfqi	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 10:43:44.527313+00
usrhyjby4skm0qsv1otng5rt5asbyr32	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 10:43:50.329161+00
sawuxjmpeyuh0q3b2c6vg6fbz22lw7fh	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 14:17:16.294623+00
dsnjbjjvoduxydlmx8ekjl6qh1w07mlb	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 14:17:16.425054+00
z1ry3diqw763ebj3n2rdqpjq9iwcp0c6	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 15:16:06.551136+00
nl3y1hdlzjm3y5p5lxizs2ljiwvr56gi	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 16:52:26.458798+00
1g54vniv6a6rjpz6dx99o2uevaaydif7	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 18:38:05.337819+00
71hwfpdu2fu3gtr0hgvgpmtzg72x8adc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-03 21:35:59.777823+00
z1cvxtvro6luiazdjqiabg9qt1kf85xy	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 01:30:12.085776+00
fgwluv8cxistrqezoxrn9vfg5vq8pmbb	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 04:26:13.63907+00
dqtwlst4fm7d5z52se5wnys3nqqc7r51	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 04:26:13.857845+00
buqey55dfgur5y4l5i2kt8gs7aalr4f3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 07:22:34.591299+00
mld82u4sl1xvhijcd22tioxeh6x8exuy	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 09:21:13.578291+00
gesdm2yt17kip308eeedna4jrd9f9c81	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 11:10:44.258673+00
q2lujug3h9ss58xk9ycitchcw7sw3um8	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 14:12:27.403917+00
x7aym6ekgrprvwbo3gvvg88gybvpp3tu	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 14:12:27.592233+00
rjysyesc5432lp940vkttjn6ech96h99	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 18:08:27.151652+00
mdixdkbdmez3rj7cr86jmhiiht7h6ara	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-04 21:09:57.497748+00
1d5j6287uqub5ifb4bkmh8lbl7f4x1mc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-05 01:10:26.535773+00
spxgn0gt7h5hpn15s73mpalicqq8ayi3	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-05 09:10:29.923685+00
iqj4key17mup3e76g816ladifs0wm3c1	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-05 09:10:33.722064+00
9x8gjpsd0kwc6og2eqbea3osbt34vhgq	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-05 13:59:47.552052+00
sf02zo89dalg66eyhjoss2sjv050ptud	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-05 13:59:47.680623+00
3r3z63x8bpxw4i0psuxcfx4fgskfe3nl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-06 00:11:38.546533+00
ekscjcmk6l9gu8kb0sxht0l92642v2o2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-06 09:35:42.886451+00
jzc2g1ax0407g3ci0yricoc3rh2ujabf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-09 09:52:07.10134+00
xkufdv09slbjdovn7b751ayvkt7njtli	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-06 10:27:18.861016+00
re06oe4woelgr1c3mvigoqmgrk8sv2x9	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-06 10:34:53.388763+00
4srd2wokkyifrlrnpjge6hmzuliri3yc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-06 15:00:27.135243+00
9ffg9zc9bq88omq0zzjerrv54bkfr9xr	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-06 15:00:27.353779+00
l8jmbojcuw9apco9q2jdpbg9adhfs5c5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-07 09:07:11.506443+00
j7oyp6gptrgk9msqzgkrim0aurjetrgf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-07 21:14:28.117181+00
k2lcoghuofyy6i74u5rehs5yunbg4ku8	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-07 21:14:28.247586+00
b1z1eyk46cu3loahbjnc5a8sq29raz2d	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-08 03:03:21.027804+00
s7okshv7563jmgp3r34ydekhtddp9gwl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-08 03:03:26.538141+00
wf2m13obty8336wbm9mc6fbw6iu69cpj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-08 09:15:13.897493+00
g2cz83cxf3r2bqef6r8ngr5defzm6pfh	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-08 19:11:31.369087+00
8l2z1daixqatdtza43p2joaoor5b9lhc	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-08 19:11:31.697605+00
mhbyn3h643ui4b54p8s1lmroq9z8mc8u	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-08 19:12:19.902118+00
1h5fxjxwlkwyprcw4qbdbkf1jx3y2m8y	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-08 19:16:00.455867+00
dwqo06vc0jm457sfoyeml8ijebhyw8ov	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-08 19:22:35.710601+00
1tahware3ksgtiw0dgnxvasa73ojxwsl	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-09 12:57:06.0782+00
j3iwups3wh3w1225wo7hdmerkwqgsgsp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-09 17:58:20.506977+00
1jv30ackeg90ryq7nr3d4cvsurxp3cfh	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-09 17:58:20.652894+00
w2dpu3ci58i90zo64aspmdlsluu4jd2p	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-09 22:44:28.915715+00
mu6rprfj5nj91bk9l60kmdwbmgw1p0fl	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-09 23:47:30.826733+00
i4rz21tvgqa5yk0s2q78j3cze99mbggp	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-10 02:05:22.684462+00
ohv6jiwbo3y8bdopf5fzvy9xslwsxavb	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-10 05:58:49.42324+00
g0yymmjzlrsux7ht31lz8v3p5eh3uwqc	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-10 05:58:49.589294+00
041qmgak2xlih5pvux7k4ufeperooj7u	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-10 12:09:22.824089+00
e6n94z6zweiutpgded7ph8p39hlpbfv5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-10 12:09:31.490489+00
tvlpl65pdlpo5exddq7m21v8kx41kahg	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-11 10:57:04.428347+00
m8r1xg2cwfhz9bdiiayx7gskwylkfnr5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-11 13:18:59.807805+00
rquszkm9pkn8clgyws4i6b40ayt0v9y5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-11 13:18:59.930612+00
ijhmoxoeytxtjivj4fv3dmhr4ay95vvz	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-11 15:12:42.757553+00
a3kt1jhf06a26nimkhi1evpccxjhaoqb	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-11 18:07:13.502112+00
4zw2kztkqg0eo7gfksw5my3ks85sl3pe	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-11 21:04:40.91737+00
3ns6zbmdj4t7913w6mqenxpxhpn5xo4g	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-12 00:59:04.723884+00
3pnflt96mwj32biafv4dj10ysi8sevuf	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-12 06:25:10.131247+00
5ajwp6h954gaz0kmxwjdxpgyhwitad2r	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-12 09:08:53.18693+00
acxszqt3b5gmwx354yfodborqbasqa2v	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-12 13:03:49.563417+00
xjivn9fe59izsoia79brw927mr41r6ce	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-12 15:45:15.662317+00
ajd2fcp26fxbt5hoyex2ytx1r828rovm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-13 09:48:31.003381+00
2ohjctz03j9lh4gi68ankgs5ujgqh12f	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-13 09:57:34.095037+00
ea6a8guwnwj836rnbvz9q19o0ybqh9vi	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 02:21:48.192981+00
b33bhp0iv21asvanjl88ohdhg442egvo	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 02:21:49.247148+00
vdy33pbry0calmqeh1u7m6uxze0nnk56	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 06:06:10.621586+00
yr2n4grvrj1fehxampecbl0a0norj0m2	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 12:11:33.773033+00
eaka8hu9fb6h2t1lkza9l8bn56howpu5	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 14:13:20.72879+00
dll6lxsb7n0rv5wu3yutyylq24mnhrmj	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 15:39:06.137235+00
bmrxkbobi75lfkhcmly7nl7mt5xgmw5s	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 15:39:06.280641+00
erjqulql77gkzvixg9gdnshy3a84791z	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-14 18:56:49.181022+00
4p3ganlhqz25o0qhw8nowtsekxotqvez	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 21:22:50.821524+00
jdrjgv9d5idnsiv6kg6vqi7qsg1eumhm	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 23:12:03.582275+00
sys9ix7in6f6wjmswk5nwrmqqhvd523q	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-14 23:12:34.823258+00
5ygdt9vtcavib0um40cm8nrone2sue85	NWY4YThmZDY1NTAzOWM1ZjIxYzQ4NDg3NjhhNzZmMjAxYmRlY2Y1NTp7ImRqYW5nb19sYW5ndWFnZSI6InBsIn0=	2014-11-14 23:12:34.853957+00
4ktqgrkwsm0l9j8xrj0z4lp82ii53q39	MzEyNTU1NzM0MDFmZDUxOTBhMDc5ODRkZjg1ODM4Y2M2OTIxZmIyYTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=	2014-11-15 03:14:46.415501+00
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: demo_dog_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_dog
    ADD CONSTRAINT demo_dog_pkey PRIMARY KEY (id);


--
-- Name: demo_dogspotuser_email_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_dogspotuser
    ADD CONSTRAINT demo_dogspotuser_email_key UNIQUE (email);


--
-- Name: demo_dogspotuser_groups_dogspotuser_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_dogspotuser_groups
    ADD CONSTRAINT demo_dogspotuser_groups_dogspotuser_id_group_id_key UNIQUE (dogspotuser_id, group_id);


--
-- Name: demo_dogspotuser_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_dogspotuser_groups
    ADD CONSTRAINT demo_dogspotuser_groups_pkey PRIMARY KEY (id);


--
-- Name: demo_dogspotuser_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_dogspotuser
    ADD CONSTRAINT demo_dogspotuser_pkey PRIMARY KEY (id);


--
-- Name: demo_dogspotuser_user_permissi_dogspotuser_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_dogspotuser_user_permissions
    ADD CONSTRAINT demo_dogspotuser_user_permissi_dogspotuser_id_permission_id_key UNIQUE (dogspotuser_id, permission_id);


--
-- Name: demo_dogspotuser_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_dogspotuser_user_permissions
    ADD CONSTRAINT demo_dogspotuser_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: demo_emailverification_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_emailverification
    ADD CONSTRAINT demo_emailverification_pkey PRIMARY KEY (id);


--
-- Name: demo_emailverification_verification_key_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_emailverification
    ADD CONSTRAINT demo_emailverification_verification_key_key UNIQUE (verification_key);


--
-- Name: demo_opinion_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_opinion
    ADD CONSTRAINT demo_opinion_pkey PRIMARY KEY (raiting_id);


--
-- Name: demo_opinionusefulnessrating_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_opinionusefulnessrating
    ADD CONSTRAINT demo_opinionusefulnessrating_pkey PRIMARY KEY (id);


--
-- Name: demo_otofoto_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_otofoto
    ADD CONSTRAINT demo_otofoto_pkey PRIMARY KEY (id);


--
-- Name: demo_raiting_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_raiting
    ADD CONSTRAINT demo_raiting_pkey PRIMARY KEY (id);


--
-- Name: demo_spot_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_spot
    ADD CONSTRAINT demo_spot_pkey PRIMARY KEY (id);


--
-- Name: demo_usersspotslist_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY demo_usersspotslist
    ADD CONSTRAINT demo_usersspotslist_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: dogspot; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_93d2d1f8; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT content_type_id_refs_id_93d2d1f8 FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_dogspotuser_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_dogspotuser_groups
    ADD CONSTRAINT demo_dogspotuser_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_dogspotuser_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_dogspotuser_user_permissions
    ADD CONSTRAINT demo_dogspotuser_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_emailverification_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_emailverification
    ADD CONSTRAINT demo_emailverification_user_id_fkey FOREIGN KEY (user_id) REFERENCES demo_dogspotuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_opinion_raiting_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_opinion
    ADD CONSTRAINT demo_opinion_raiting_id_fkey FOREIGN KEY (raiting_id) REFERENCES demo_raiting(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_opinionusefulnessrating_opinion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_opinionusefulnessrating
    ADD CONSTRAINT demo_opinionusefulnessrating_opinion_id_fkey FOREIGN KEY (opinion_id) REFERENCES demo_opinion(raiting_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_opinionusefulnessrating_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_opinionusefulnessrating
    ADD CONSTRAINT demo_opinionusefulnessrating_user_id_fkey FOREIGN KEY (user_id) REFERENCES demo_dogspotuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_raiting_spot_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_raiting
    ADD CONSTRAINT demo_raiting_spot_id_fkey FOREIGN KEY (spot_id) REFERENCES demo_spot(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_raiting_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_raiting
    ADD CONSTRAINT demo_raiting_user_id_fkey FOREIGN KEY (user_id) REFERENCES demo_dogspotuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_usersspotslist_spot_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_usersspotslist
    ADD CONSTRAINT demo_usersspotslist_spot_id_fkey FOREIGN KEY (spot_id) REFERENCES demo_spot(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demo_usersspotslist_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_usersspotslist
    ADD CONSTRAINT demo_usersspotslist_user_id_fkey FOREIGN KEY (user_id) REFERENCES demo_dogspotuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dogspotuser_id_refs_id_95a62f0b; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_dogspotuser_groups
    ADD CONSTRAINT dogspotuser_id_refs_id_95a62f0b FOREIGN KEY (dogspotuser_id) REFERENCES demo_dogspotuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dogspotuser_id_refs_id_9d253855; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY demo_dogspotuser_user_permissions
    ADD CONSTRAINT dogspotuser_id_refs_id_9d253855 FOREIGN KEY (dogspotuser_id) REFERENCES demo_dogspotuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_261dba70; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT user_id_refs_id_261dba70 FOREIGN KEY (user_id) REFERENCES demo_dogspotuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_af469daa; Type: FK CONSTRAINT; Schema: public; Owner: dogspot
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT user_id_refs_id_af469daa FOREIGN KEY (user_id) REFERENCES demo_dogspotuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

