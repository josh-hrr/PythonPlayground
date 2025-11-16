class LibraryError(Exception):
  pass

class InvalidTitleError(LibraryError):
  pass

class BookIsNotAvailableError(LibraryError):
  pass

class UserNotFoundError(LibraryError):
  pass