import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = ""
port = 8888

p1 = [100, 100, 0.0]
p2 = [700, 100, 3.0]
p3 = [100, 500, 0.0]
p4 = [700, 500, 3.0]

p1_health = 30
p2_health = 30
p3_health = 30
p4_health = 30

bullets = []

server_socket.bind((host, port))
# print "Server bounded."

players = {"1": "", "2": "", "3": "", "4": ""}
addrs = []

def restart_values():
    global p1
    global p2
    global p3
    global p4
    global p1_health
    global p2_health
    global p3_health
    global p4_health
    global bullets

    p1 = [100, 100, 0.0]
    p2 = [700, 100, 3.0]
    p3 = [100, 500, 0.0]
    p4 = [700, 500, 3.0]

    p1_health = 30
    p2_health = 30
    p3_health = 30
    p4_health = 30

    bullets = []

while True:
    try:
        msg, addr = server_socket.recvfrom(2048)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print message
        msg, addr = "", ()
    if msg != "":
        code = msg[:2]
        # print "start - ", msg, code, addr
        if code == "00":
            if addr not in addrs:
                if players["1"] == "":
                    players["1"] = addr
                    addrs.append(addr)
                    server_socket.sendto("You are player #1", addr)
                    server_socket.sendto("zz,1," + str(p1[0]) + "," + str(p1[1]) + "," + str(p1[2]), addr)
                    server_socket.sendto("zz,2," + str(p2[0]) + "," + str(p2[1]) + "," + str(p2[2]), addr)
                    server_socket.sendto("zz,3," + str(p3[0]) + "," + str(p3[1]) + "," + str(p3[2]), addr)
                    server_socket.sendto("zz,4," + str(p4[0]) + "," + str(p4[1]) + "," + str(p4[2]), addr)
                    for addr in addrs:
                        server_socket.sendto("T,Player #1 Connected,5,400", addr)
                elif players["2"] == "":
                    players["2"] = addr
                    addrs.append(addr)
                    server_socket.sendto("You are player #2", addr)
                    server_socket.sendto("zz,1," + str(p1[0]) + "," + str(p1[1]) + "," + str(p1[2]), addr)
                    server_socket.sendto("zz,2," + str(p2[0]) + "," + str(p2[1]) + "," + str(p2[2]), addr)
                    server_socket.sendto("zz,3," + str(p3[0]) + "," + str(p3[1]) + "," + str(p3[2]), addr)
                    server_socket.sendto("zz,4," + str(p4[0]) + "," + str(p4[1]) + "," + str(p4[2]), addr)
                    for addr in addrs:
                        server_socket.sendto("T,Player #2 Connected,5,400", addr)
                elif players["3"] == "":
                    players["3"] = addr
                    addrs.append(addr)
                    server_socket.sendto("You are player #3", addr)
                    server_socket.sendto("zz,1," + str(p1[0]) + "," + str(p1[1]) + "," + str(p1[2]), addr)
                    server_socket.sendto("zz,2," + str(p2[0]) + "," + str(p2[1]) + "," + str(p2[2]), addr)
                    server_socket.sendto("zz,3," + str(p3[0]) + "," + str(p3[1]) + "," + str(p3[2]), addr)
                    server_socket.sendto("zz,4," + str(p4[0]) + "," + str(p4[1]) + "," + str(p4[2]), addr)
                    for addr in addrs:
                        server_socket.sendto("T,Player #3 Connected,5,400", addr)
                elif players["4"] == "":
                    players["4"] = addr
                    addrs.append(addr)
                    server_socket.sendto("You are player #4", addr)
                    server_socket.sendto("zz,1," + str(p1[0]) + "," + str(p1[1]) + "," + str(p1[2]), addr)
                    server_socket.sendto("zz,2," + str(p2[0]) + "," + str(p2[1]) + "," + str(p2[2]), addr)
                    server_socket.sendto("zz,3," + str(p3[0]) + "," + str(p3[1]) + "," + str(p3[2]), addr)
                    server_socket.sendto("zz,4," + str(p4[0]) + "," + str(p4[1]) + "," + str(p4[2]), addr)
                    for addr in addrs:
                        server_socket.sendto("T,Player #4 Connected,5,400", addr)
                else:
                    server_socket.sendto("Maximum number of players connected.", addr)
        elif code == "11":
            # print 'Getting pos#1'
            data = msg[2:]
            if data is not None and data != "" and p1 is not None:
                # print data, addr
                data = data.split(',')
                for i in xrange(len(data) - 1):
                    p1[i] = int(data[i])
                p1[2] = data[2]
                for addr in addrs:
                    server_socket.sendto("zz,1," + str(p1[0]) + "," + str(p1[1]) + "," + str(p1[2]), addr)
            else:
                p1 = None
        elif code == "12":
            # print 'Getting pos#2'
            data = msg[2:]
            if data is not None and data != "" and p2 is not None:
                # print data, addr
                data = data.split(',')
                for i in xrange(len(data) - 1):
                    p2[i] = int(data[i])
                p2[2] = data[2]
                for addr in addrs:
                    server_socket.sendto("zz,2," + str(p2[0]) + "," + str(p2[1]) + "," + str(p2[2]), addr)
            else:
                p2 = None
        elif code == "13":
            # print 'Getting pos#3'
            data = msg[2:]
            if data is not None and data != "" and p3 is not None:
                # print data, addr
                data = data.split(',')
                for i in xrange(len(data) - 1):
                    p3[i] = int(data[i])
                p3[2] = data[2]
                for addr in addrs:
                    server_socket.sendto("zz,3," + str(p3[0]) + "," + str(p3[1]) + "," + str(p3[2]), addr)
            else:
                p3 = None
        elif code == "14":
            # print 'Getting pos#4'
            data = msg[2:]
            if data is not None and data != "" and p4 is not None:
                # print data, addr
                data = data.split(',')
                for i in xrange(len(data) - 1):
                    p4[i] = int(data[i])
                p4[2] = data[2]
                for addr in addrs:
                    server_socket.sendto("zz,4," + str(p4[0]) + "," + str(p4[1]) + "," + str(p4[2]), addr)
            else:
                p4 = None

        elif code == "20":
            data = msg[2:]
            data = data.split(",")
            text = data[1]
            x = data[2]
            y = data[3]
            for addr in addrs:
                server_socket.sendto("T," + text + "," + x + "," + y, addr)

        elif code == "21":
            # print 'Getting killed'
            data = msg[2:]
            data = data.split(',')
            killer = data[1]
            for addr in addrs:
                server_socket.sendto("T,Player #" + killer + " killed Player #1,5,400", addr)

        elif code == "22":
            # print 'Getting killed'
            data = msg[2:]
            data = data.split(',')
            killer = data[1]
            for addr in addrs:
                server_socket.sendto("T,Player #" + killer + " killed Player #2,5,400", addr)

        elif code == "23":
            # print 'Getting killed'
            data = msg[2:]
            data = data.split(',')
            killer = data[1]
            for addr in addrs:
                server_socket.sendto("T,Player #" + killer + " killed Player #3,5,400", addr)

        elif code == "24":
            # print 'Getting killed'
            data = msg[2:]
            data = data.split(',')
            killer = data[1]
            for addr in addrs:
                server_socket.sendto("T,Player #" + killer + " killed Player #4,5,400", addr)

        elif code == "31":
            # print 'Sending pos#1'
            server_socket.sendto(str(p1[0]) + "," + str(p1[1]) + "," + str(p1[2]), addr)
        elif code == "32":
            # print 'Sending pos#2'
            server_socket.sendto(str(p2[0]) + "," + str(p2[1]) + "," + str(p2[2]), addr)
        elif code == "33":
            # print 'Sending pos#3'
            server_socket.sendto(str(p3[0]) + "," + str(p3[1]) + "," + str(p3[2]), addr)
        elif code == "34":
            # print 'Sending pos#4'
            server_socket.sendto(str(p4[0]) + "," + str(p4[1]) + "," + str(p4[2]), addr)

        elif code == "40":
            # print 'Getting bullet'
            data = msg[2:]
            # print data, addr
            data = data.split(',')
            if [str(data[0]), float(data[1]), int(data[2]), int(data[3])] not in bullets:
                bullets.append([str(data[0]), float(data[1]), int(data[2]), int(data[3])])
                s = "["
                for bullet in bullets:
                    s += "["
                    for n in bullet:
                        s += str(n) + "$"
                    s = s[:-1]
                    s += "]#"
                s = s[:-1]
                s += "]"
                for addr in addrs:
                    server_socket.sendto("B," + s, addr)

        elif code == "50":
            length = len(bullets)
            # print 'Deleting bullet'
            data = msg[2:]
            # print data, addr
            data = data.split(',')
            # print data, bullets
            try:
                bullets.remove([str(data[0]), float(data[1]), int(data[2]), int(data[3])])
            except ValueError as e:
                print e.message
                # print "DELETE FAILED"
            s = "["
            for bullet in bullets:
                s += "["
                for n in bullet:
                    s += str(n) + "$"
                s = s[:-1]
                s += "]#"
            s = s[:-1] if len(s) > 1 else s
            s += "]"
            for addr in addrs:
                # print len("B," + s)
                # print "B," + s
                server_socket.sendto("B," + s, addr)

        elif code == "61":
            data = msg[2:]
            p1[2] = data

        elif code == "62":
            data = msg[2:]
            p2[2] = data

        elif code == "63":
            data = msg[2:]
            p3[2] = data

        elif code == "64":
            data = msg[2:]
            p4[2] = data

        elif code == "71":
            data = msg[2:]
            data = data.split(",")
            hitter = data[1]
            p1_health -= 1
            for addr in addrs:
                server_socket.sendto("hp,1," + str(p1_health) + "," + hitter, addr)

        elif code == "72":
            data = msg[2:]
            data = data.split(",")
            hitter = data[1]
            p2_health -= 1
            for addr in addrs:
                server_socket.sendto("hp,2," + str(p2_health) + "," + hitter, addr)

        elif code == "73":
            data = msg[2:]
            data = data.split(",")
            hitter = data[1]
            p3_health -= 1
            for addr in addrs:
                server_socket.sendto("hp,3," + str(p3_health) + "," + hitter, addr)

        elif code == "74":
            data = msg[2:]
            data = data.split(",")
            hitter = data[1]
            p4_health -= 1
            for addr in addrs:
                server_socket.sendto("hp,4," + str(p4_health) + "," + hitter, addr)

        elif code == "81":
            data = msg[2:]

        elif code == "99":
            if players["1"] == addr:
                players["1"] = ""
                addrs.remove(addr)
                for address in addrs:
                    server_socket.sendto("T,Player #1 Disconnected,5,400", address)
            elif players["2"] == addr:
                players["2"] = ""
                addrs.remove(addr)
                for address in addrs:
                    server_socket.sendto("T,Player #2 Disconnected,5,400", address)
            elif players["3"] == addr:
                players["3"] = ""
                addrs.remove(addr)
                for address in addrs:
                    server_socket.sendto("T,Player #3 Disconnected,5,400", address)
            elif players["4"] == addr:
                players["4"] = ""
                addrs.remove(addr)
                for address in addrs:
                    server_socket.sendto("T,Player #4 Disconnected,5,400", address)

        else:
            server_socket.sendto("Wrong code. " + code, addr)
