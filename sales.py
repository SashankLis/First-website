import Snowflake as sf


def sales_load():


    #truncate tmp table SALES

    # truncate_tmp_sales = '''
    #                             TRUNCATE TABLE BHATBHATENI.SASHANK_TMP.TMP_SALES
    #                            '''
    #
    # sf.execute_query(truncate_tmp_sales)


    #load tmp table SALES

    # load_temp_sales = '''
    #                     INSERT INTO BHATBHATENI.SASHANK_TMP.TMP_SALES(
    #                     SLS_ID, STORE_KY,
    #                     PDT_KY, CUSTOMER_KY,TRANSACTION_TIME,
    #                     QTY,AMT,DSCNT
    #                     )
    #                     SELECT SLS.ID,LOC.LOCN_KY,
    #                     ITM.PDT_KY,CUST.CUSTOMER_KY,TRANSACTION_TIME,QUANTITY,AMOUNT,DISCOUNT
    #                     FROM BHATBHATENI.SASHANK_STG.STG_SALES SLS
    #                     LEFT JOIN BHATBHATENI.SASHANK_TGT.TGT_STORE LOC
    #                     ON SLS.STORE_ID = LOC.LOCN_ID
    #                     LEFT JOIN BHATBHATENI.SASHANK_TGT.TGT_PRODUCT ITM
    #                     ON SLS.PRODUCT_ID = ITM.PDT_ID
    #                     LEFT JOIN BHATBHATENI.SASHANK_TGT.TGT_CUSTOMER CUST
    #                     ON CUST.CUSTOMER_ID = SLS.CUSTOMER_ID;
    #                     '''
    # sf.execute_query(load_temp_sales)


    #load target table SALES


    load_tgt_sales = '''
                        INSERT INTO BHATBHATENI.SASHANK_TGT.TGT_SALES(
                        SLS_KY,
                        SLS_ID,LOCN_KY,PDT_KY,CUSTOMER_KY,
                        TRANSACTION_TIME,QTY,AMT,DSCNT,OPEN_CLOSE_CD,
                        ROW_INSRT_TMS, ROW_UPDT_TMS
                        )
                        SELECT SLS_KY,SLS_ID,STORE_KY,PDT_KY,CUSTOMER_KY,TRANSACTION_TIME,
                        QTY,AMT,DSCNT,1,LOCALTIMESTAMP,LOCALTIMESTAMP
                        FROM  BHATBHATENI.SASHANK_TMP.TMP_SALES
                        WHERE SLS_ID NOT IN (SELECT DISTINCT SLS_ID FROM BHATBHATENI.SASHANK_TGT.TGT_SALES)
                        '''
    sf.execute_query(load_tgt_sales)

    # update target table SALES

    # update_tgt_sales = '''
    #                         UPDATE BHATBHATENI.SASHANK_TGT.TGT_SALES AS T1
    #                         SET T1.LOCN_KY = T2.STORE_KY,
    #                         T1.PDT_KY = T2.PDT_KY,
    #                         T1.CUSTOMER_KY = T2.CUSTOMER_KY,
    #                         T1.QTY = T1.QTY + T2.QTY,
    #                         T1.AMT = T1.AMT + T2.AMT,
    #                         T1.DSCNT = T1.DSCNT+ T2.DSCNT,
    #                         ROW_UPDT_TMS = LOCALTIMESTAMP
    #                         FROM BHATBHATNEI.SASHANK_TMP.TMP_SALES AS T2
    #                         WHERE T1.SLS_ID = T2.SLS_ID;
    #                         '''
    #
    # sf.execute_query(update_tgt_sales)