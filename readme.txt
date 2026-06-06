Per poter eseguire la pipeline è necessario avviare i vari container. Per fare ciò è possibile eseguire lo script all_up.sh se si vogliono istanziare tutti i container. IN alternativa, se si vuole eseguire una fase per volta è possibile eseguire:
- data_ingestion_uni_hdfs.sh per la fase di data ingestion dal server remoto a HDFS. Se si istanziano i container HDFS per la prima volta è necessario eseguire lo script HDFS_init.sh, altrimenti si esegue HDFS_start.sh
- data_ingestion_hdfs_redis.sh per la trasferire i risultati delle query da HDFS a Redis
- data_processing.sh per il processamento dei dati
- Grafana.sh per la visualizzazione dei risultati delle query

Data Ingestion da server remoto a HDFS
Per avviare la pipeline di NiFi è necessario accedere a NiFi mediante le credenziali username:admin, password:ProgettoSabd2026. Nella cartella docker/NiFi sono presenti i file JSON da caricare tramite interfaccia grafica se il container è stato avviato la prima volta.
Per fare ciò è necessario trascinare un processor group e importare il file uni_server_to_hdfs. Successivamente, eseguire la pipeline. La pipeline può essere eseguita senza interromperla poichè la PutHDFS salva i file insingola copia.

Spark
Per avviare la pipeline di processamento sono disponibili i file scripts/spark_submit_df.sh e scripts/submit_rdd.sh. Se si vuole trasferire i dati su Grafana è necessario eseguire lo script scripts/spark_submit.sh, in quanto i processor a monte della pipeline individuano i file nella directory di destinazione delle query eseguite con Dataframe.

Data ingestion da HDFS a Redis
Per avviare la pipeline di trasferimento dei dati da HDFS a Redis è necessario imposrtare il file JSON hdfs_to_redis.json in modo analogo a quanto fatto nella fase di data ingestion precedente.

Visualizzazione dati con Grafana
Per visualizzare i dati con Grafana è necessario creare una dashboard importando il file JSON situato nella cartella docker/Grafana.