DROP TABLE IF EXISTS event CASCADE;
DROP TABLE IF EXISTS salle CASCADE;
DROP TABLE IF EXISTS activities CASCADE;

DROP SEQUENCE IF EXISTS id_event_seq ;
DROP SEQUENCE IF EXISTS id_type_event_seq ;
CREATE SEQUENCE id_event_seq ;
CREATE SEQUENCE id_type_event_seq ;


CREATE TABLE type_event (
	id_type_event integer NOT NULL DEFAULT nextval
	('id_type_event_seq'::regclass) PRIMARY KEY,
	label_type_event text
);

INSERT INTO type_event (id_type_event, label_type_event) VALUES
(1, 'scholar'),
(2, 'sport')
;

CREATE TABLE event (
	id_event integer NOT NULL DEFAULT nextval
	('id_event_seq'::regclass),
  nom text COLLATE pg_catalog."default" NOT NULL,
  description text COLLATE pg_catalog."default",
  type_event integer,
  CONSTRAINT event_pkey PRIMARY KEY (id_event),
  CONSTRAINT event_nom_key UNIQUE (nom),
  CONSTRAINT event_type_event_fkey FOREIGN KEY (type_event)
      REFERENCES public.type_event (id_type_event) MATCH SIMPLE
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

INSERT INTO event (id_event,nom, description, type_event) VALUES
(1,'reunion1', 'Reunion marketing', 1),
(2,'Running', ' ', 2)
;

-- CREATE TABLE statistique_monstre
-- (
--     id_monstre integer NOT NULL,
--     force integer,
--     magie integer,
--     agilite integer,
--     defense integer,
--     points_de_vie integer,
--     CONSTRAINT statistique_monstre_pkey PRIMARY KEY (id_monstre),
--     CONSTRAINT statistique_monstre_id_monstre_fkey FOREIGN KEY (id_monstre)
--         REFERENCES public.monstre (id_monstre) MATCH SIMPLE
--         ON UPDATE CASCADE
--         ON DELETE CASCADE
-- );
--
-- INSERT INTO statistique_monstre (id_monstre, force, magie, agilite, defense, points_de_vie) VALUES
-- (1,60,0,20,50,1500),
-- (2,30,0,10,20,400),
-- (3,5,30,30,20,300),
-- (4,15,15,15,15,300),
-- (5,100,100,50,100,3000),
-- (6,20,0,10,20,200),
-- (7,40,50,40,30,800),
-- (8,70,0,20,80,5000),
-- (9,50,30,0,45,1250),
-- (10,100,30,100,80,600),
-- (11,20,50,20,100,450),
-- (12,800,800,800,800,10000),
-- (13,1500,1500,300,1500,20000),
-- (14,60,150,50,50,400),
-- (15,30,100,80,50,163),
-- (16,50,150,30,80,480),
-- (17,80,120,180,65,190),
-- (18,50,0,30,80,1000),
-- (19,600,600,600,600,7000);

ALTER SEQUENCE id_event_seq RESTART WITH 2;
ALTER SEQUENCE id_type_event_seq RESTART WITH 11;

