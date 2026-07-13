from database.DB_connect import DBConnect
from model.actor import Actor


class DAO():
    @staticmethod
    def getAllActor():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select n.*
                    from role_mapping rm, names n 
                    where rm.name_id = n.id and 
                    (rm.category = "actress" or rm.category ='actor')
                    and n.date_of_birth < "2026-07-12" """

        cursor.execute(query)

        for row in cursor:
            result.append(
                Actor(
                    id = row["id"],
                    name = row["name"],
                    height = row["height"],
                    date_of_birth = row["date_of_birth"],
                    known_for_movies = row["known_for_movies"]
                )
            )

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi(rangeA, rangeB):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
                select attori.id as id, rm.movie_id,r.avg_rating 
                from role_mapping rm , (select n.*
                                        from role_mapping rm, names n 
                                        where rm.name_id = n.id and 
                                        (rm.category = "actress" or rm.category ='actor')
                                        and n.date_of_birth < "2026-07-12" ) as attori, ratings r
                where rm.name_id = attori.id and r.movie_id = rm.movie_id and avg_rating >= %s and avg_rating <= %s 
                group by attori.id, rm.movie_id 
                order by attori.id asc 
         """

        cursor.execute(query,(rangeA, rangeB))

        for row in cursor:
            result.append(row["id"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(rangeA, rangeB):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
                    select rm2.movie_id , rm2.name_id as u ,rm.name_id as v, m.worlwide_gross_income as peso
                    from role_mapping rm, role_mapping rm2, movie m, ratings r 
                    where rm2.movie_id = rm.movie_id and rm2.name_id < rm.name_id and m.id = rm2.movie_id and m.worlwide_gross_income is not null and 
                    r.movie_id = rm2.movie_id and r.avg_rating >= %s and r.avg_rating <= %s
                    order by rm2.movie_id asc 
             """

        cursor.execute(query,(rangeA, rangeB))

        for row in cursor:
            result.append((row["u"], row["v"], row["peso"]))

        cursor.close()
        conn.close()
        return result
