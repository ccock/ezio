/*
 @ 0xCCCCCCCC
*/

#ifndef EZIO_SOCKET_ADDRESS_H_
#define EZIO_SOCKET_ADDRESS_H_

#include <string>

#include "kbase/basic_macros.h"

#include "ezio/endian_utils.h"

#if defined(OS_POSIX)
#include <arpa/inet.h>
#elif defined(OS_WIN)
#include <WinSock2.h>
#endif

namespace ezio {

class SocketAddress {
public:
    explicit SocketAddress(const sockaddr_in& addr);

    explicit SocketAddress(unsigned short port);

    SocketAddress(const std::string& ip, unsigned short port);

    DEFAULT_COPY(SocketAddress);

    DEFAULT_MOVE(SocketAddress);

    unsigned short port() const noexcept
    {
        return NetworkToHost(addr_.sin_port);
    }

    const sockaddr_in& raw() const noexcept
    {
        return addr_;
    }

    const std::string& ToHostPort() const noexcept
    {
        return host_port_;
    }

private:
    sockaddr_in addr_;
    std::string host_port_;
};

}   // namespace ezio

#endif  // EZIO_SOCKET_ADDRESS_H_
