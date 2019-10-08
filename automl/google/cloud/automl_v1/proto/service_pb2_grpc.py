# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.automl_v1.proto import (
    dataset_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_dataset__pb2,
)
from google.cloud.automl_v1.proto import (
    model_evaluation_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_model__evaluation__pb2,
)
from google.cloud.automl_v1.proto import (
    model_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_model__pb2,
)
from google.cloud.automl_v1.proto import (
    service_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class AutoMlStub(object):
    """AutoML Server API.

  The resource names are assigned by the server.
  The server never reuses names that it has created after the resources with
  those names are deleted.

  An ID of a resource is the last element of the item's resource name. For
  `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then
  the id for the item is `{dataset_id}`.

  Currently the only supported `location_id` is "us-central1".

  On any input that is documented to expect a string parameter in
  snake_case or kebab-case, either of those cases is accepted.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateDataset = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/CreateDataset",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.CreateDatasetRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetDataset = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/GetDataset",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.GetDatasetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_dataset__pb2.Dataset.FromString,
        )
        self.ListDatasets = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/ListDatasets",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListDatasetsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListDatasetsResponse.FromString,
        )
        self.UpdateDataset = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/UpdateDataset",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.UpdateDatasetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_dataset__pb2.Dataset.FromString,
        )
        self.DeleteDataset = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/DeleteDataset",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.DeleteDatasetRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ImportData = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/ImportData",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ImportDataRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ExportData = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/ExportData",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ExportDataRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.CreateModel = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/CreateModel",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.CreateModelRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetModel = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/GetModel",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.GetModelRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_model__pb2.Model.FromString,
        )
        self.ListModels = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/ListModels",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListModelsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListModelsResponse.FromString,
        )
        self.DeleteModel = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/DeleteModel",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.DeleteModelRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.UpdateModel = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/UpdateModel",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.UpdateModelRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_model__pb2.Model.FromString,
        )
        self.GetModelEvaluation = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/GetModelEvaluation",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.GetModelEvaluationRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_model__evaluation__pb2.ModelEvaluation.FromString,
        )
        self.ListModelEvaluations = channel.unary_unary(
            "/google.cloud.automl.v1.AutoMl/ListModelEvaluations",
            request_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListModelEvaluationsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListModelEvaluationsResponse.FromString,
        )


class AutoMlServicer(object):
    """AutoML Server API.

  The resource names are assigned by the server.
  The server never reuses names that it has created after the resources with
  those names are deleted.

  An ID of a resource is the last element of the item's resource name. For
  `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then
  the id for the item is `{dataset_id}`.

  Currently the only supported `location_id` is "us-central1".

  On any input that is documented to expect a string parameter in
  snake_case or kebab-case, either of those cases is accepted.
  """

    def CreateDataset(self, request, context):
        """Creates a dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetDataset(self, request, context):
        """Gets a dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListDatasets(self, request, context):
        """Lists datasets in a project.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateDataset(self, request, context):
        """Updates a dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteDataset(self, request, context):
        """Deletes a dataset and all of its contents.
    Returns empty response in the
    [response][google.longrunning.Operation.response] field when it completes,
    and `delete_details` in the
    [metadata][google.longrunning.Operation.metadata] field.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ImportData(self, request, context):
        """Imports data into a dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExportData(self, request, context):
        """Exports dataset's data to the provided output location.
    Returns an empty response in the
    [response][google.longrunning.Operation.response] field when it completes.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateModel(self, request, context):
        """Creates a model.
    Returns a Model in the [response][google.longrunning.Operation.response]
    field when it completes.
    When you create a model, several model evaluations are created for it:
    a global evaluation, and one evaluation for each annotation spec.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetModel(self, request, context):
        """Gets a model.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListModels(self, request, context):
        """Lists models.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteModel(self, request, context):
        """Deletes a model.
    Returns `google.protobuf.Empty` in the
    [response][google.longrunning.Operation.response] field when it completes,
    and `delete_details` in the
    [metadata][google.longrunning.Operation.metadata] field.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateModel(self, request, context):
        """Updates a model.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetModelEvaluation(self, request, context):
        """Gets a model evaluation.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListModelEvaluations(self, request, context):
        """Lists model evaluations.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AutoMlServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateDataset": grpc.unary_unary_rpc_method_handler(
            servicer.CreateDataset,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.CreateDatasetRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetDataset": grpc.unary_unary_rpc_method_handler(
            servicer.GetDataset,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.GetDatasetRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_dataset__pb2.Dataset.SerializeToString,
        ),
        "ListDatasets": grpc.unary_unary_rpc_method_handler(
            servicer.ListDatasets,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListDatasetsRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListDatasetsResponse.SerializeToString,
        ),
        "UpdateDataset": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateDataset,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.UpdateDatasetRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_dataset__pb2.Dataset.SerializeToString,
        ),
        "DeleteDataset": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteDataset,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.DeleteDatasetRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ImportData": grpc.unary_unary_rpc_method_handler(
            servicer.ImportData,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ImportDataRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ExportData": grpc.unary_unary_rpc_method_handler(
            servicer.ExportData,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ExportDataRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "CreateModel": grpc.unary_unary_rpc_method_handler(
            servicer.CreateModel,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.CreateModelRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetModel": grpc.unary_unary_rpc_method_handler(
            servicer.GetModel,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.GetModelRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_model__pb2.Model.SerializeToString,
        ),
        "ListModels": grpc.unary_unary_rpc_method_handler(
            servicer.ListModels,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListModelsRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListModelsResponse.SerializeToString,
        ),
        "DeleteModel": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteModel,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.DeleteModelRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "UpdateModel": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateModel,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.UpdateModelRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_model__pb2.Model.SerializeToString,
        ),
        "GetModelEvaluation": grpc.unary_unary_rpc_method_handler(
            servicer.GetModelEvaluation,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.GetModelEvaluationRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_model__evaluation__pb2.ModelEvaluation.SerializeToString,
        ),
        "ListModelEvaluations": grpc.unary_unary_rpc_method_handler(
            servicer.ListModelEvaluations,
            request_deserializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListModelEvaluationsRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1_dot_proto_dot_service__pb2.ListModelEvaluationsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.automl.v1.AutoMl", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
