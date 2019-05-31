# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: stats.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import stats_pb2


class StatsBase(abc.ABC):

    @abc.abstractmethod
    async def GetMonthStat(self, stream):
        pass

    @abc.abstractmethod
    async def GetCategoryStat(self, stream):
        pass

    @abc.abstractmethod
    async def GetMonthAmountStat(self, stream):
        pass

    def __mapping__(self):
        return {
            '/stats.Stats/GetMonthStat': grpclib.const.Handler(
                self.GetMonthStat,
                grpclib.const.Cardinality.UNARY_UNARY,
                stats_pb2.LogItemQueryMessage,
                stats_pb2.ImageMessage,
            ),
            '/stats.Stats/GetCategoryStat': grpclib.const.Handler(
                self.GetCategoryStat,
                grpclib.const.Cardinality.UNARY_UNARY,
                stats_pb2.LogItemQueryMessage,
                stats_pb2.ImageMessage,
            ),
            '/stats.Stats/GetMonthAmountStat': grpclib.const.Handler(
                self.GetMonthAmountStat,
                grpclib.const.Cardinality.UNARY_UNARY,
                stats_pb2.LogItemQueryMessage,
                stats_pb2.ImageMessage,
            ),
        }


class StatsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetMonthStat = grpclib.client.UnaryUnaryMethod(
            channel,
            '/stats.Stats/GetMonthStat',
            stats_pb2.LogItemQueryMessage,
            stats_pb2.ImageMessage,
        )
        self.GetCategoryStat = grpclib.client.UnaryUnaryMethod(
            channel,
            '/stats.Stats/GetCategoryStat',
            stats_pb2.LogItemQueryMessage,
            stats_pb2.ImageMessage,
        )
        self.GetMonthAmountStat = grpclib.client.UnaryUnaryMethod(
            channel,
            '/stats.Stats/GetMonthAmountStat',
            stats_pb2.LogItemQueryMessage,
            stats_pb2.ImageMessage,
        )