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

INSERT INTO event (id_event,nom, description, type_event_id) VALUES
(1,'reunion1', 'Reunion marketing', 0),
(2,'Running', ' ', 1)
;


ALTER SEQUENCE id_event_seq RESTART WITH 2;
ALTER SEQUENCE id_type_event_seq RESTART WITH 11;

