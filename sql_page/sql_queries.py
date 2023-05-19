from django.db import connection
from sql_page.input_operations import input_to_list, input_to_int, format_data

def SQL_1(input):
    try:
        with connection.cursor() as cursor:
            list_of_inputs = input_to_int(input_to_list(input, 1))
            cursor.execute("""
            SELECT sql_page_user.login, sql_page_rating.rating
            FROM sql_page_user
            INNER JOIN sql_page_rating ON sql_page_user.id = sql_page_rating.user_id
            ORDER BY sql_page_rating.rating DESC
            LIMIT %s""", list_of_inputs)
            """"Find top-<n> users by rating (Expects 1 input: <n: int>)"""
            row = cursor.fetchall()

        if row:
            columns = cursor.description
            column_names = [column[0] for column in columns]
            formatted_row = format_data(column_names, row)
            return formatted_row
        else:
            return 'Nothing found...'
    except Exception as e:
        return f"SQL/Validation Error: {str(e)}"


def SQL_2(input):
    try:
        with connection.cursor() as cursor:
            list_of_inputs = input_to_list(input, 1)
            cursor.execute("""
             SELECT sql_page_champion.name, sql_page_statistics.avg_kills, sql_page_statistics.winrate, sql_page_statistics.rating  
             FROM sql_page_champion INNER JOIN sql_page_infoall ON sql_page_champion.id = sql_page_infoall.champion_id
             INNER JOIN sql_page_user ON sql_page_infoall.user_id = sql_page_user.id
             INNER JOIN sql_page_statistics ON sql_page_statistics.id = sql_page_infoall.statistics_id
             WHERE sql_page_user.login = %s""", list_of_inputs)
            """Find stats on champions by <user_login> (Expects 1 input: <login:text>)"""
            row = cursor.fetchall()

        if row:
            columns = cursor.description
            column_names = [column[0] for column in columns]
            formatted_row = format_data(column_names, row)
            return formatted_row
        else:
            return 'Nothing found...'
    except Exception as e:
        return f"SQL/Validation Error: {str(e)}"

def SQL_3(input):
    try:
        with connection.cursor() as cursor:
            list_of_inputs = input_to_list(input, 2)
            try:
                list_of_inputs[0] = int(list_of_inputs[0])
            except Exception as e:
                raise ValueError("First Input contains string characters, integer expected!")
            cursor.execute("""
            SELECT sql_page_user.login
            FROM sql_page_user INNER JOIN sql_page_infoall ON sql_page_user.id = sql_page_infoall.user_id
            INNER JOIN sql_page_champion ON sql_page_infoall.champion_id = sql_page_champion.id
            INNER JOIN sql_page_statistics ON sql_page_statistics.id = sql_page_infoall.statistics_id
            WHERE sql_page_statistics.winrate > %s AND sql_page_champion.name = %s""", list_of_inputs)
            """Find all users which have winrate over <x> for champion <champ_name> (Expects 2 inputs: <winrate: int>, <champ_name: text>)"""
            row = cursor.fetchall()
        if row:
            columns = cursor.description
            column_names = [column[0] for column in columns]
            formatted_row = format_data(column_names, row)
            return formatted_row
        else:
            return 'Nothing found...'
    except Exception as e:
        return f"SQL/Validation Error: {str(e)}"

def SQL_4(input):
    try:
        with connection.cursor() as cursor:
            list_of_inputs = input_to_int(input_to_list(input, 1))
            cursor.execute("""
                SELECT sql_page_champion.name
                FROM sql_page_champion
                WHERE sql_page_champion.id IN (
                    SELECT sql_page_video.champion_id
                    FROM sql_page_video
                    GROUP BY sql_page_video.champion_id
                    HAVING COUNT(sql_page_video.champion_id) > %s)""", list_of_inputs)
            """Find all champions that have more than <videos_count> videos (Expects 1 input: <videos_count: int>)"""
            row = cursor.fetchall()

        if row:
            columns = cursor.description
            column_names = [column[0] for column in columns]
            formatted_row = format_data(column_names, row)
            return formatted_row
        else:
            return 'Nothing found...'
    except Exception as e:
        return f"SQL/Validation Error: {str(e)}"


def SQL_5(input):
    try:
        with connection.cursor() as cursor:
            list_of_inputs = input_to_list(input,1)
            cursor.execute("""
               SELECT pc_y.name
               FROM sql_page_champion pc_x
               JOIN sql_page_itemschampions pci_x ON pc_x.id = pci_x.champion_id
               JOIN sql_page_items pi_x ON pci_x.item_id = pi_x.id
               JOIN sql_page_itemschampions pci_y ON pci_x.item_id = pci_y.item_id
               JOIN sql_page_champion pc_y ON pci_y.champion_id = pc_y.id
               WHERE pc_x.name = %s
                    AND pc_y.name <> %s
               GROUP BY pc_y.id, pc_y.age, pc_y.phrase, pc_y.name
               HAVING COUNT(DISTINCT pci_y.item_id) = (
                    SELECT COUNT(DISTINCT pci_x.item_id)
                    FROM sql_page_champion pc_x
                    JOIN sql_page_itemschampions pci_x ON pc_x.id = pci_x.champion_id
                    WHERE pc_x.name = %s)""", 3 * list_of_inputs)
            """Find all the champions who have at least all the items that champion "name" has (Expects 1 input: <name: str>)"""
            row = cursor.fetchall()

        if row:
            columns = cursor.description
            column_names = [column[0] for column in columns]
            formatted_row = format_data(column_names, row)
            return formatted_row
        else:
            return 'Nothing found...'
    except Exception as e:
        return f"SQL/Validation Error: {str(e)}"

def SQL_6(input):
    try:
        with connection.cursor() as cursor:
            list_of_inputs = input_to_list(input, 2)
            try:
                list_of_inputs[1] = int(list_of_inputs[1])
            except Exception as e:
                raise ValueError("Second Input contains string characters, integer expected!")
            cursor.execute("""
            SELECT c.name AS champion_name
            FROM sql_page_champion c
            JOIN sql_page_infoall i ON c.id = i.champion_id
            JOIN sql_page_statistics s ON i.statistics_id = s.id
            JOIN sql_page_user u ON i.user_id = u.id
            WHERE u.login = %s AND i.season = %s
            ORDER BY s.winrate DESC
            LIMIT 1""", list_of_inputs)
            """Find the champion whose user "login" in season "x" has the best win rate (Expects 2 input: {login: str, x: int }"""
            row = cursor.fetchall()

        if row:
            columns = cursor.description
            column_names = [column[0] for column in columns]
            formatted_row = format_data(column_names, row)
            return formatted_row
        else:
            return 'Nothing found...'
    except Exception as e:
        return f"SQL/Validation Error: {str(e)}"

def SQL_7(input):
    try:
        with connection.cursor() as cursor:
            list_of_inputs = input_to_list(input, 1)
            cursor.execute("""
                            SELECT u.name AS user_name, c.name AS champion_name, s.rating
                            FROM sql_page_user u
                            JOIN sql_page_infoall i ON u.id = i.user_id
                            JOIN sql_page_champion c ON i.champion_id = c.id
                            JOIN sql_page_statistics s ON i.statistics_id = s.id
                            WHERE c.name = %s
                            ORDER BY s.rating DESC
                            LIMIT 1""", list_of_inputs)
            """Find user whose is the best on following champion "x" by rating (Expects 1 input: {x: str}"""
            row = cursor.fetchall()
        if row:
            columns = cursor.description
            column_names = [column[0] for column in columns]
            formatted_row = format_data(column_names, row)
            return formatted_row
        else:
            return 'Nothing found...'
    except Exception as e:
        return f"SQL/Validation Error: {str(e)}"

def SQL_8(input):
    try:
        with connection.cursor() as cursor:
            list_of_inputs = input_to_list(input, 1)
            try:
                list_of_inputs[0] = int(list_of_inputs[0])
            except Exception as e:
                raise ValueError("Input contains string characters, integer expected!")
            cursor.execute("""
                           SELECT u.name AS "user", c.name AS "champion", s.avg_kills, s.rating, s.winrate
                           FROM sql_page_user u
                           JOIN sql_page_infoall i ON u.id = i.user_id
                           JOIN sql_page_statistics s ON i.statistics_id = s.id
                           JOIN sql_page_champion c ON i.champion_id = c.id
                           LIMIT %s""", list_of_inputs)
            """Find all users stats for each champion limiting by "x" records(Expects 1 input: {x: int}"""
            row = cursor.fetchall()
        if row:
            columns = cursor.description
            column_names = [column[0] for column in columns]
            formatted_row = format_data(column_names, row)
            return formatted_row
        else:
            return 'Nothing found...'
    except Exception as e:
        return f"SQL/Validation Error: {str(e)}"