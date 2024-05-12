import helper_functions


def lambda_handler(event, context):

    values = helper_functions.get_indices_value()
    helper_functions.send_message(values)

    return {
        'statusCode': 200,
    }


if __name__ == "__main__":
    lambda_handler(None, None)
