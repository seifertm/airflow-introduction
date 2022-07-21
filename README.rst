====================
Airflow Introduction
====================

This repository contains exercises to convey the basic principles of Apache Airflow.

Setup
=====

Linux/MacOS
-----------
.. code:: bash

    git clone https://github.com/seifertm/airflow-introduction.git
    cd airflow-introduction
    python -m venv venv
    . venv/bin/activate
    pip install apache-airflow==2.3.3
    export AIRFLOW_HOME="${PWD}"
    export AIRFLOW__CORE__LOAD_EXAMPLES="false"
    airflow standalone


Windows
-------

Airflow has no native Windows support. You will have to set up WSL2. Please install "Ubuntu on Windows" from the Windows Store and run the following commands in a Ubuntu shell:

.. code:: bash

    git clone https://github.com/seifertm/airflow-introduction.git
    cd airflow-introduction
    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt install python3.8-venv
    python3 -m venv venv
    . venv/bin/activate
    pip install apache-airflow==2.3.3
    pip install flask-appbuilder
    export AIRFLOW_HOME="${PWD}"
    export AIRFLOW__CORE__LOAD_EXAMPLES="false"
    airflow standalone


Log into the Airflow UI (http://localhost:8080) using the credentials presented on the terminal.

Exercises
=========
Exercise 0
----------
Run `my_first_dag` using the Web UI. Take some minutes to explore the web interface.


Exercise 1
----------
Remove task `C` from the DAG definition. Run the DAG again and make sure it reflects the new structure.

Airflow will pick up changes to DAGs on its own after some time. In order to speed up the process, you can use the airflow command ``airflow dags reserialize``. Don't forget to set the ``AIRFLOW_HOME`` environment variable correctly if you run the command in a new shell.


Exercise 2
----------
The current DAG uses EmptyOperator only. Change Task `A` to use Airflow's `BashOperator`_. The operator's requires a bash_command to know what it's supposed to do. The command should print your name using ``echo``.

Run the DAG and check the task's logs to make sure your DAG does what it should.

.. _BashOperator: https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/bash/index.html


Exercise 3
----------
Change Task `B` to use Airflow's `PythonOperator`_. The operator should call a Python function that fetches your name from the previous task and returns the string `Hello` followed by the name that was retrieved.

.. _PythonOperator: https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html#airflow.operators.python.PythonOperator


Exercise 4
----------
Schedule `my_first_dag` to run every three minutes (see `Running DAGs <https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html#running-dags>`__). Check the calendar view of the DAG in the web interface to make sure that the changes have been picked up.


Exercise 5
----------
Extend `my_first_dag` with a sensor. The sensor should check for a specific file on your file system. If the file exists, the sensor continues. Airflow provides `FileSensor`_ for that purpose. Note that FileSensor uses the "fs_default" Airflow connection to resolve the specified file path. This connection defaults to "/". You need to adjust the fs_default connection in the web interface or specify the file path accordingly for the sensor to work.

The sensor should be the first task of the DAG. Other tasks are only executed if the sensor finds the file it is looking for.

You are adding a sensor to a scheduled DAG. If the file cannot be found the sensor will run for a longer period than three minutes. This will cause multiple DAG runs to be started, each with the own sensor that are polling for the file. To avoid such a build-up of queued Airflow tasks, add the keyword argument `max_active_runs=1 <https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/dag/index.html?highlight=max_active_runs#airflow.models.dag.DagModel.max_active_runs>`__ to your Airflow DAG.

.. _FileSensor: https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/sensors/filesystem/index.html


Exercise 6
----------
Think of possible applications of Airflow in your project. Be ready to explain the business case you are trying to solve. The explanation should be very high-level so that participants can understand it even if they work in different areas. Be ready to discuss if Airflow is a good fit.
