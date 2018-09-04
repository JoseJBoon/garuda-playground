import grpc

from garuda_dir import garuda_pb2 as messages, garuda_pb2_grpc as client


class Client:
    def run(self):
        channel = grpc.insecure_channel('localhost:50051')
        # response = client.GarudaStub(channel).ReadArticle(messages.ID(id=1))

        response = client.GarudaStub(channel).CreateBook(messages.Book(name='Awesome Book'))

        print(response)


if __name__ == '__main__':
    Client().run()
