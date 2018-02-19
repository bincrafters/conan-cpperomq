#include <cstdlib>
#include <iostream>
#include <string>
#include <CpperoMQ/All.hpp>

int main()
{
    using namespace CpperoMQ;

    Context context;

    PullSocket pull_socket(context.createPullSocket());
    pull_socket.bind("inproc://example");

    PushSocket push_socket(context.createPushSocket());
    push_socket.connect("inproc://example");

    push_socket.send(OutgoingMessage("Hello, CpperoMQ!"));

    IncomingMessage msg;
    pull_socket.receive(msg);

    std::string str(msg.charData(), msg.size());
    std::cout << str << std::endl;

    return EXIT_SUCCESS;
}
