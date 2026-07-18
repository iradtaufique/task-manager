-- ─────────────────────────────────────────────────────────────
-- Task Manager — Database Seed File
-- Run this file in MySQL Workbench to set up the initial schema
-- ─────────────────────────────────────────────────────────────

CREATE DATABASE IF NOT EXISTS task_manager_db;
USE task_manager_db;

CREATE TABLE IF NOT EXISTS tasks (
    id          INT          NOT NULL AUTO_INCREMENT,
    title       VARCHAR(255) NOT NULL,
    description TEXT,
    status      ENUM('pending', 'in_progress', 'done') NOT NULL DEFAULT 'pending',
    completed   BOOLEAN      NOT NULL DEFAULT FALSE,
    created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

INSERT INTO tasks (title, description, status, completed)
VALUES
    ('Set up GitHub repository',   'Init repo, add gitignore, push to GitHub',  'done',        TRUE),
    ('Learn MySQL fundamentals',   'Data types, CRUD queries, WHERE and ORDER BY', 'in_progress', FALSE),
    ('Build Django models',        'Define Task model and connect to MySQL',     'pending',     FALSE),
    ('Create REST API with DRF',   'Serializers, ViewSets, URL routing',         'pending',     FALSE),
    ('Build React task list',      'Fetch and display tasks using useEffect',    'pending',     FALSE),
    ('Add create task form',       'POST new tasks to the Django API',           'pending',     FALSE),
    ('Implement edit and delete',  'PUT and DELETE requests from React',         'pending',     FALSE),
    ('Write GitHub Actions CI',    'Run Django tests and React lint on every PR','pending',     FALSE),
    ('Write README documentation', 'Badges, setup guide, API reference table',  'pending',     FALSE);