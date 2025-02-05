# frozen_string_literal: true

require "ostruct"
require "json"

module SeedExamplesClient
  class Types
    class Request
      # @return [Object]
      attr_reader :request
      # @return [OpenStruct] Additional properties unmapped to the current class definition
      attr_reader :additional_properties
      # @return [Object]
      attr_reader :_field_set
      protected :_field_set

      OMIT = Object.new

      # @param request [Object]
      # @param additional_properties [OpenStruct] Additional properties unmapped to the current class definition
      # @return [SeedExamplesClient::Types::Request]
      def initialize(request:, additional_properties: nil)
        @request = request
        @additional_properties = additional_properties
        @_field_set = { "request": request }
      end

      # Deserialize a JSON object to an instance of Request
      #
      # @param json_object [String]
      # @return [SeedExamplesClient::Types::Request]
      def self.from_json(json_object:)
        struct = JSON.parse(json_object, object_class: OpenStruct)
        request = struct["request"]
        new(request: request, additional_properties: struct)
      end

      # Serialize an instance of Request to a JSON object
      #
      # @return [String]
      def to_json(*_args)
        @_field_set&.to_json
      end

      # Leveraged for Union-type generation, validate_raw attempts to parse the given
      #  hash and check each fields type against the current object's property
      #  definitions.
      #
      # @param obj [Object]
      # @return [Void]
      def self.validate_raw(obj:)
        obj.request.is_a?(Object) != false || raise("Passed value for field obj.request is not the expected type, validation failed.")
      end
    end
  end
end
