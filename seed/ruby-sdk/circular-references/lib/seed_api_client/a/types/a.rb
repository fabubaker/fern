# frozen_string_literal: true

require "json"

module SeedApiClient
  module A
    class A
      attr_reader :s, :additional_properties

      # @param s [String]
      # @param additional_properties [OpenStruct] Additional properties unmapped to the current class definition
      # @return [A::A]
      def initialize(s:, additional_properties: nil)
        # @type [String]
        @s = s
        # @type [OpenStruct] Additional properties unmapped to the current class definition
        @additional_properties = additional_properties
      end

      # Deserialize a JSON object to an instance of A
      #
      # @param json_object [JSON]
      # @return [A::A]
      def self.from_json(json_object:)
        struct = JSON.parse(json_object, object_class: OpenStruct)
        s = struct.s
        new(s: s, additional_properties: struct)
      end

      # Serialize an instance of A to a JSON object
      #
      # @return [JSON]
      def to_json(*_args)
        { "s": @s }.to_json
      end

      # Leveraged for Union-type generation, validate_raw attempts to parse the given hash and check each fields type against the current object's property definitions.
      #
      # @param obj [Object]
      # @return [Void]
      def self.validate_raw(obj:)
        obj.s.is_a?(String) != false || raise("Passed value for field obj.s is not the expected type, validation failed.")
      end
    end
  end
end
