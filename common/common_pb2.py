# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12\x06\x63ommon\x1a\x1fgoogle/protobuf/timestamp.proto\"\x07\n\x05\x45mpty\"M\n\x0b\x41\x63kResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\",\n\x0bListRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\"\xb0\x02\n\x0bTradePublic\x12\x10\n\x08trade_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x03\x12\x10\n\x08quantity\x18\x04 \x01(\x03\x12\x33\n\x0forder_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x0e\x61ggressor_side\x18\x06 \x01(\x0e\x32\x16.common.OrderDirection\x12\x14\n\x0c\x62uy_order_id\x18\x08 \x01(\t\x12\x15\n\rsell_order_id\x18\t \x01(\t\x12\x13\n\x0b\x62uy_user_id\x18\n \x01(\t\x12\x14\n\x0csell_user_id\x18\x0b \x01(\t\x12\x0f\n\x07\x62uy_fee\x18\x0c \x01(\x03\x12\x10\n\x08sell_fee\x18\r \x01(\x03\"E\n\x13GetUserLimitRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x0e\n\x06offset\x18\x03 \x01(\x05\"q\n\x0cTradesPublic\x12#\n\x06trades\x18\x01 \x03(\x0b\x32\x13.common.TradePublic\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"\x1e\n\x0bUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"1\n\x0eOrderBookEntry\x12\r\n\x05price\x18\x01 \x01(\x04\x12\x10\n\x08quantity\x18\x02 \x01(\x04\"\xc3\x01\n\tOrderBook\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x04\x62ids\x18\x03 \x03(\x0b\x32\x16.common.OrderBookEntry\x12$\n\x04\x61sks\x18\x04 \x03(\x0b\x32\x16.common.OrderBookEntry\x12\x19\n\x11last_traded_price\x18\x05 \x01(\x04\x12\x10\n\x08sequence\x18\x06 \x01(\x04\"\x9f\x02\n\rBalancePublic\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65posit\x18\x03 \x01(\x03\x12\x14\n\x0crealised_pnl\x18\x04 \x01(\x03\x12\x14\n\x0corder_margin\x18\x05 \x01(\x03\x12\x17\n\x0fposition_margin\x18\x06 \x01(\x03\x12\x16\n\x0eunrealised_pnl\x18\x07 \x01(\x03\x12\x19\n\x11\x61vailable_balance\x18\x08 \x01(\x03\x12\x13\n\x0bnet_funding\x18\t \x01(\x03\x12\x0c\n\x04\x66\x65\x65s\x18\n \x01(\x03\x12\x16\n\x0eis_institution\x18\x32 \x01(\x08\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd9\t\n\x12\x41ppendOrderRequest\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12$\n\x04side\x18\x03 \x01(\x0e\x32\x16.common.OrderDirection\x12\x1f\n\x04type\x18\x04 \x01(\x0e\x32\x11.common.OrderType\x12/\n\rtime_in_force\x18\x05 \x01(\x0e\x32\x18.common.OrderTimeInForce\x12.\n\x0corder_action\x18\x06 \x01(\x0e\x32\x13.common.OrderActionH\x00\x88\x01\x01\x12\x10\n\x08quantity\x18\x07 \x01(\x04\x12\r\n\x05price\x18\x08 \x01(\x04\x12\x0f\n\x07user_id\x18\n \x01(\t\x12\x19\n\x0cold_quantity\x18\x0b \x01(\x04H\x01\x88\x01\x01\x12\x16\n\told_price\x18\x0c \x01(\x04H\x02\x88\x01\x01\x12\x17\n\x0f\x63lient_order_id\x18\r \x01(\t\x12\x13\n\x0bpassive_qty\x18\x0e \x01(\x04\x12(\n\x08\x62\x65st_bid\x18\x14 \x01(\x0b\x32\x16.common.OrderBookEntry\x12(\n\x08\x62\x65st_ask\x18\x15 \x01(\x0b\x32\x16.common.OrderBookEntry\x12)\n\x0corder_status\x18\x32 \x01(\x0e\x32\x13.common.OrderStatus\x12\x17\n\nis_passive\x18\x33 \x01(\x08H\x03\x88\x01\x01\x12;\n\x17port_ingress_entry_time\x18< \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16port_ingress_exit_time\x18= \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x1fuser_service_ingress_entry_time\x18> \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x1euser_service_ingress_exit_time\x18? \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11\x65ngine_entry_time\x18@ \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10\x65ngine_exit_time\x18\x41 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x1euser_service_egress_entry_time\x18\x42 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x1duser_service_egress_exit_time\x18\x43 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16port_egress_entry_time\x18\x44 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x0e\x63orrelation_id\x18\x62 \x01(\tH\x04\x88\x01\x01\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0f\n\r_order_actionB\x0f\n\r_old_quantityB\x0c\n\n_old_priceB\r\n\x0b_is_passiveB\x11\n\x0f_correlation_id\"Y\n\tUnderlier\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x04\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"z\n\x0b\x46undingRate\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04rate\x18\x02 \x01(\x03\x12\x1e\n\x16time_remaining_seconds\x18\x03 \x01(\x04\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"}\n\x11\x41llOrdersResponse\x12*\n\x06orders\x18\x01 \x03(\x0b\x32\x1a.common.AppendOrderRequest\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"\x8e\x01\n\x0bTradeVolume\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x14\n\x0ctrade_amount\x18\x02 \x01(\x03\x12\x14\n\x0ctrade_volume\x18\x03 \x01(\x03\x12\x14\n\x0cprice_change\x18\x04 \x01(\x03\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa7\x01\n\x0e\x43\x61ndleInternal\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04open\x18\x03 \x01(\x04\x12\x0c\n\x04high\x18\x04 \x01(\x04\x12\x0b\n\x03low\x18\x05 \x01(\x04\x12\r\n\x05\x63lose\x18\x06 \x01(\x04\x12\x0e\n\x06volume\x18\x07 \x01(\x04\x12\x0e\n\x06period\x18\x08 \x01(\x04*+\n\tOrderType\x12\t\n\x05LIMIT\x10\x00\x12\n\n\x06MARKET\x10\x01\x12\x07\n\x03\x41LO\x10\x03*#\n\x0eOrderDirection\x12\x07\n\x03\x42UY\x10\x00\x12\x08\n\x04SELL\x10\x01*-\n\x10OrderTimeInForce\x12\x07\n\x03GTC\x10\x00\x12\x07\n\x03IOC\x10\x01\x12\x07\n\x03\x46OK\x10\x02*8\n\x0bOrderAction\x12\x07\n\x03NEW\x10\x00\x12\n\n\x06MODIFY\x10\x01\x12\n\n\x06\x43\x41NCEL\x10\x02\x12\x08\n\x04\x46ILL\x10\x04*\x96\x05\n\x0bOrderStatus\x12\x07\n\x03\x41\x43K\x10\x00\x12\n\n\x06\x46ILLED\x10\x02\x12\x0c\n\x08MODIFIED\x10\x14\x12\r\n\tCANCELLED\x10\x1e\x12\x11\n\rCANCELLED_STP\x10\x1f\x12\x0c\n\x08REJECTED\x10\x32\x12\x11\n\rNO_SUCH_ORDER\x10\x34\x12\x16\n\x12INVALID_ORDER_TYPE\x10\x35\x12\x0e\n\nBAD_SYMBOL\x10\x36\x12\x1d\n\x19PRICE_LESS_THAN_MIN_PRICE\x10\x37\x12 \n\x1cPRICE_GREATER_THAN_MAX_PRICE\x10\x38\x12\x1e\n\x1a\x43\x41NNOT_MODIFY_PARTIAL_FILL\x10:\x12\x17\n\x13\x46\x41ILED_MARGIN_CHECK\x10<\x12%\n!INVALID_TICK_SIZE_PRECISION_PRICE\x10?\x12(\n$INVALID_TICK_SIZE_PRECISION_QUANTITY\x10@\x12#\n\x1fQUANTITY_LESS_THAN_MIN_QUANTITY\x10\x41\x12&\n\"QUANTITY_GREATER_THAN_MAX_QUANTITY\x10\x42\x12(\n$REJECTED_GREATER_THAN_MAX_PRICE_BAND\x10\x43\x12%\n!REJECTED_LESS_THAN_MIN_PRICE_BAND\x10\x44\x12\x19\n\x15INVALID_TIME_IN_FORCE\x10\x45\x12&\n\"REJECTED_WOULD_BREACH_MAX_POSITION\x10\x46\x12\x1f\n\x1b\x43\x41NNOT_MODIFY_NO_SUCH_ORDER\x10G\x12\x1a\n\x16REJECTED_MARKET_CLOSED\x10H\x12\x10\n\x0cRATE_LIMITED\x10\x61*6\n\x0cSymbolStatus\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\x0c\n\x08\x44\x45LISTED\x10\x02*\x87\x01\n\x0f\x43\x61ndlesInterval\x12\x0e\n\nONE_MINUTE\x10\x00\x12\x10\n\x0c\x46IVE_MINUTES\x10\x02\x12\x13\n\x0f\x46IFTEEN_MINUTES\x10\x03\x12\x12\n\x0eTHIRTY_MINUTES\x10\x04\x12\x0c\n\x08ONE_HOUR\x10\x05\x12\x0e\n\nFOUR_HOURS\x10\x06\x12\x0b\n\x07ONE_DAY\x10\x07\x42<\n\x0f\x63om.qfex.commonP\x01Z\'github.com/QFEX-org/proto/common;commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.qfex.commonP\001Z\'github.com/QFEX-org/proto/common;common'
  _globals['_ORDERTYPE']._serialized_start=3156
  _globals['_ORDERTYPE']._serialized_end=3199
  _globals['_ORDERDIRECTION']._serialized_start=3201
  _globals['_ORDERDIRECTION']._serialized_end=3236
  _globals['_ORDERTIMEINFORCE']._serialized_start=3238
  _globals['_ORDERTIMEINFORCE']._serialized_end=3283
  _globals['_ORDERACTION']._serialized_start=3285
  _globals['_ORDERACTION']._serialized_end=3341
  _globals['_ORDERSTATUS']._serialized_start=3344
  _globals['_ORDERSTATUS']._serialized_end=4006
  _globals['_SYMBOLSTATUS']._serialized_start=4008
  _globals['_SYMBOLSTATUS']._serialized_end=4062
  _globals['_CANDLESINTERVAL']._serialized_start=4065
  _globals['_CANDLESINTERVAL']._serialized_end=4200
  _globals['_EMPTY']._serialized_start=57
  _globals['_EMPTY']._serialized_end=64
  _globals['_ACKRESPONSE']._serialized_start=66
  _globals['_ACKRESPONSE']._serialized_end=143
  _globals['_LISTREQUEST']._serialized_start=145
  _globals['_LISTREQUEST']._serialized_end=189
  _globals['_TRADEPUBLIC']._serialized_start=192
  _globals['_TRADEPUBLIC']._serialized_end=496
  _globals['_GETUSERLIMITREQUEST']._serialized_start=498
  _globals['_GETUSERLIMITREQUEST']._serialized_end=567
  _globals['_TRADESPUBLIC']._serialized_start=569
  _globals['_TRADESPUBLIC']._serialized_end=682
  _globals['_USERREQUEST']._serialized_start=684
  _globals['_USERREQUEST']._serialized_end=714
  _globals['_ORDERBOOKENTRY']._serialized_start=716
  _globals['_ORDERBOOKENTRY']._serialized_end=765
  _globals['_ORDERBOOK']._serialized_start=768
  _globals['_ORDERBOOK']._serialized_end=963
  _globals['_BALANCEPUBLIC']._serialized_start=966
  _globals['_BALANCEPUBLIC']._serialized_end=1253
  _globals['_APPENDORDERREQUEST']._serialized_start=1256
  _globals['_APPENDORDERREQUEST']._serialized_end=2497
  _globals['_UNDERLIER']._serialized_start=2499
  _globals['_UNDERLIER']._serialized_end=2588
  _globals['_FUNDINGRATE']._serialized_start=2590
  _globals['_FUNDINGRATE']._serialized_end=2712
  _globals['_ALLORDERSRESPONSE']._serialized_start=2714
  _globals['_ALLORDERSRESPONSE']._serialized_end=2839
  _globals['_TRADEVOLUME']._serialized_start=2842
  _globals['_TRADEVOLUME']._serialized_end=2984
  _globals['_CANDLEINTERNAL']._serialized_start=2987
  _globals['_CANDLEINTERNAL']._serialized_end=3154
# @@protoc_insertion_point(module_scope)
