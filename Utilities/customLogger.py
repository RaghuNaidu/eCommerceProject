import logging


class LogGen:

    @staticmethod
    def loggen():
        logger=logging.getLogger()
        fhandler=logging.FileHandler(filename='.//Logs//automation.log',mode="a")
        formatter=logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                    datefmt='%m-%d %H:%M')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
