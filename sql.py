#Use DISTINCT to avoid duplicates.
UPDATE PARTY_ARRANGEMENT_RLTSHP_STGNG stg
SET party_id = (SELECT DISTINCT xref.party_id 
                FROM party_xref xref
                WHERE stg.party_local_id = xref.party_local_id
                  AND stg.party_source_sys_code = xref.party_source_sys_code);


# It’s always a good practice to explicitly specify the target columns in the INSERT INTO
INSERT INTO PARTY_ARRANGEMENT_RLTSHP (party_id, PARTY_AR_RLTSHP_TYPE_CDE, PARTY_AR_RLTSHP_TYPE_DESC)
SELECT party_id, PARTY_AR_RLTSHP_TYPE_CDE, PARTY_AR_RLTSHP_TYPE_DESC
FROM PARTY_ARRANGEMENT_RLTSHP_STGNG 
WHERE party_id IS NOT NULL;
