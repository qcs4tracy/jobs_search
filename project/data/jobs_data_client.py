import grpc.beta.implementations as impl
from project import conf
import jobs_pb2

class JobInfoClient(object):

    def __init__(self):
        server_port = conf.PROTOBUF_SERVER['listen_port']
        server_host = conf.PROTOBUF_SERVER['host']
        self.__channel = impl.insecure_channel(server_host, server_port)
        self.__stub = jobs_pb2.beta_create_JobsService_stub(self.__channel)

    def JobCount(self, request=None, timeout=30):
        if request is None:
            request = jobs_pb2.Void()
        res = self.__stub.GetCount(request, timeout)
        return res.number

    ## temporary only fetch without condition or predicate filters
    def FetchJobs(self, offset=0, limit=20, timeout=30):
        batch = self.__stub.GetJobs(jobs_pb2.SearchOptions(offset=offset, resultLimit=limit), timeout)
        res = []
        for job in batch:
            res.append(self._jobToDict(job))
        return res

    def _jobToDict(self, job):
        """
        :arg:  job
        :type: jobs_pb2.JobInfo
        :rtype: dict
        """
        job_dict = {}
        job_dict['id_icims'] = job.id_icims
        job_dict['title'] = job.title
        job_dict['location'] = job.location
        job_dict['description_short'] = job.description_short
        job_dict['feed_date'] = job.feed_date
        job_dict['time_ago'] = job.time_ago
        return job_dict

if __name__ == '__main__':
    db = JobInfoClient()
    x = db.JobCount()
    x