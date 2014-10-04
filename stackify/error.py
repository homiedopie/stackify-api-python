import traceback
import sys

from stackify.formats import JSONObject


class ErrorItem(JSONObject):
    def __init__(self):
        self.Message = None # exception message
        self.ErrorType = None # exception class name
        self.ErrorTypeCode = None # ?
        self.Data = None # custom data
        self.SourceMethod = None
        self.StackTrace = [] # array of TraceFrames
        self.InnerError = None # cause?

    def load_stack(self, tb):
        stacks = traceback.extract_tb(tb)
        for filename, lineno, parent, method in stacks:
            self.StackTrace.append(TraceFrame(filename, lineno, method))


class TraceFrame(JSONObject):
    def __init__(self, filename, lineno, method):
        self.CodeFileName = filename
        self.LineNum = lineno
        self.Method = method


class WebRequestDetail(JSONObject):
    def __init__(self):
        self.UserIPAddress = None
        self.HttpMethod = None
        self.RequestProtocol = None
        self.RequestUrl = None
        self.RequestUrlRoot = None
        self.ReferralUrl = None
        self.Headers = {}
        self.Cookies = {}
        self.QueryString = {}
        self.PostData = {}
        self.SessionData = {}
        self.PostDataRaw = None
        self.MVCAction = None
        self.MVCController = None
        self.MVCArea = None


class StackifyError(JSONObject):
    def __init__(self):
        self.EnvironmentDetail = None # environment detail object
        self.OccurredEpochMillis = None
        self.Error = None # ErrorItem object
        self.WebRequestDetail = None # WebRequestDetail object
        self.CustomerName = None
        self.UserName = None

    def load_exception(self):
        self.Error = ErrorItem()
        type_, value, tb = sys.exc_info()
        self.Error.load_stack(tb)

