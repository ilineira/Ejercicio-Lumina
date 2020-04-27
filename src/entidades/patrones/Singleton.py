import threading


class Singleton(object):

    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            cls.__singleton_lock.acquire()
            if not cls.__singleton_instance:
                cls.__singleton_instance = cls()
            cls.__singleton_lock.release()
        return cls.__singleton_instance
