from database.DB_connect import DBConnect
from model.actor import Actor


class DAO():
    @staticmethod
    def getAllActor():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select distinct n.*
                    from names n ,role_mapping rm 
                    where n.id = rm.name_id 
                    and (rm.category = 'actor' or rm.category ='actress') 
                    and n.date_of_birth is not null 
                    and n.date_of_birth < "2026-07-12" 
        """

        cursor.execute(query)

        for row in cursor:
           result.append(
               Actor(
                   id_attore = row["id"],
                   name = row["name"],
                   height =  row["height"],
                   date_of_birth = row["date_of_birth"],
                   known_for_movies= row["known_for_movies"]
               )
           )

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getActorValutation(rangeA, rangeB):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select rm.name_id as id_actor, m.id ,m.title, r.avg_rating 
                    from role_mapping rm ,movie m ,ratings r 
                    where m.id = rm.movie_id and m.id=r.movie_id and r.avg_rating >= %s and r.avg_rating <= %s
                    order by rm.name_id, m.id 
            """

        cursor.execute(query, (rangeA,rangeB))

        for row in cursor:
            result.append(
                 row["id_actor"]
            )

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(rangeA,rangeB):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select m.title , rm.name_id as u , rm2.name_id as v, m.worlwide_gross_income as peso
                    from role_mapping rm ,role_mapping rm2,movie m, ratings r
                    where rm.movie_id = rm2.movie_id and  m.id = rm2.movie_id and r.movie_id = m.id 
                    and rm.name_id < rm2.name_id 
                    and r.avg_rating >= %s and r.avg_rating <= %s
                    and m.worlwide_gross_income is not null
                    order by m.title 
                """

        cursor.execute(query, (rangeA, rangeB))

        for row in cursor:
            result.append( (row["u"], row["v"], row["peso"])

            )

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllRatings():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """SELECT distinct (avg_rating) as voto
                    FROM ratings r 
                    order by avg_rating asc 
                    """

        cursor.execute(query)

        for row in cursor:
            result.append(row["voto"])

        cursor.close()
        conn.close()
        return result


