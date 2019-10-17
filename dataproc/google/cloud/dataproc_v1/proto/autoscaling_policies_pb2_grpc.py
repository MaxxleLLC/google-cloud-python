# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.dataproc_v1.proto import (
    autoscaling_policies_pb2 as google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AutoscalingPolicyServiceStub(object):
    """The API interface for managing autoscaling policies in the
  Google Cloud Dataproc API.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateAutoscalingPolicy = channel.unary_unary(
            "/google.cloud.dataproc.v1.AutoscalingPolicyService/CreateAutoscalingPolicy",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.CreateAutoscalingPolicyRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.AutoscalingPolicy.FromString,
        )
        self.UpdateAutoscalingPolicy = channel.unary_unary(
            "/google.cloud.dataproc.v1.AutoscalingPolicyService/UpdateAutoscalingPolicy",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.UpdateAutoscalingPolicyRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.AutoscalingPolicy.FromString,
        )
        self.GetAutoscalingPolicy = channel.unary_unary(
            "/google.cloud.dataproc.v1.AutoscalingPolicyService/GetAutoscalingPolicy",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.GetAutoscalingPolicyRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.AutoscalingPolicy.FromString,
        )
        self.ListAutoscalingPolicies = channel.unary_unary(
            "/google.cloud.dataproc.v1.AutoscalingPolicyService/ListAutoscalingPolicies",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.ListAutoscalingPoliciesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.ListAutoscalingPoliciesResponse.FromString,
        )
        self.DeleteAutoscalingPolicy = channel.unary_unary(
            "/google.cloud.dataproc.v1.AutoscalingPolicyService/DeleteAutoscalingPolicy",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.DeleteAutoscalingPolicyRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class AutoscalingPolicyServiceServicer(object):
    """The API interface for managing autoscaling policies in the
  Google Cloud Dataproc API.
  """

    def CreateAutoscalingPolicy(self, request, context):
        """Creates new autoscaling policy.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateAutoscalingPolicy(self, request, context):
        """Updates (replaces) autoscaling policy.

    Disabled check for update_mask, because all updates will be full
    replacements.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetAutoscalingPolicy(self, request, context):
        """Retrieves autoscaling policy.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListAutoscalingPolicies(self, request, context):
        """Lists autoscaling policies in the project.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteAutoscalingPolicy(self, request, context):
        """Deletes an autoscaling policy. It is an error to delete an autoscaling
    policy that is in use by one or more clusters.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AutoscalingPolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateAutoscalingPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.CreateAutoscalingPolicy,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.CreateAutoscalingPolicyRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.AutoscalingPolicy.SerializeToString,
        ),
        "UpdateAutoscalingPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateAutoscalingPolicy,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.UpdateAutoscalingPolicyRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.AutoscalingPolicy.SerializeToString,
        ),
        "GetAutoscalingPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.GetAutoscalingPolicy,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.GetAutoscalingPolicyRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.AutoscalingPolicy.SerializeToString,
        ),
        "ListAutoscalingPolicies": grpc.unary_unary_rpc_method_handler(
            servicer.ListAutoscalingPolicies,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.ListAutoscalingPoliciesRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.ListAutoscalingPoliciesResponse.SerializeToString,
        ),
        "DeleteAutoscalingPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteAutoscalingPolicy,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_autoscaling__policies__pb2.DeleteAutoscalingPolicyRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dataproc.v1.AutoscalingPolicyService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
