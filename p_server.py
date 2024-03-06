from concurrent import futures
import grpc
import records_pb2
import records_pb2_grpc

class FileServiceServicer(records_pb2_grpc.FileServiceServicer):
    def Upload(self, request, context):
        filename = request.filename
        message = "File " + filename + " upload successful"
        print(message)
        return records_pb2.UploadResponse(message=message)

    def Download(self, request, context):
        filename = request.filename
        message = "File " + filename + " download successful" 
        print(message)
        file = records_pb2.File(content=message)
        return records_pb2.DownloadResponse(file=file)

def serve():
    print("P Server on port 4999")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    records_pb2_grpc.add_FileServiceServicer_to_server(FileServiceServicer(), server)
    server.add_insecure_port('[::]:4999')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
