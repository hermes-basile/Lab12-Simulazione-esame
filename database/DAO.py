from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """ inserire la query """

        cursor.execute(query)

        for row in cursor:
            res.append(Esempio(
                nome = row["nome_della_riga_query"]
            ))


        cursor.close()
        conn.close()
        return res

