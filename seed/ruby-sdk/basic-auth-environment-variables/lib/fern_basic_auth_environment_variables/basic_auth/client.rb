# frozen_string_literal: true

require_relative "../../requests"
require "json"
require "async"

module SeedBasicAuthEnvironmentVariablesClient
  class BasicAuthClient
    # @return [SeedBasicAuthEnvironmentVariablesClient::RequestClient]
    attr_reader :request_client

    # @param request_client [SeedBasicAuthEnvironmentVariablesClient::RequestClient]
    # @return [SeedBasicAuthEnvironmentVariablesClient::BasicAuthClient]
    def initialize(request_client:)
      @request_client = request_client
    end

    # GET request with basic auth scheme
    #
    # @param request_options [SeedBasicAuthEnvironmentVariablesClient::RequestOptions]
    # @return [Boolean]
    def get_with_basic_auth(request_options: nil)
      response = @request_client.conn.get do |req|
        req.options.timeout = request_options.timeout_in_seconds unless request_options&.timeout_in_seconds.nil?
        req.headers["username"] = request_options.username unless request_options&.username.nil?
        req.headers["password"] = request_options.password unless request_options&.password.nil?
        req.headers = { **req.headers, **(request_options&.additional_headers || {}) }.compact
        req.url "#{@request_client.get_url(request_options: request_options)}/basic-auth"
      end
      JSON.parse(response.body)
    end

    # POST request with basic auth scheme
    #
    # @param request [Object]
    # @param request_options [SeedBasicAuthEnvironmentVariablesClient::RequestOptions]
    # @return [Boolean]
    def post_with_basic_auth(request: nil, request_options: nil)
      response = @request_client.conn.post do |req|
        req.options.timeout = request_options.timeout_in_seconds unless request_options&.timeout_in_seconds.nil?
        req.headers["username"] = request_options.username unless request_options&.username.nil?
        req.headers["password"] = request_options.password unless request_options&.password.nil?
        req.headers = { **req.headers, **(request_options&.additional_headers || {}) }.compact
        req.body = { **(request || {}), **(request_options&.additional_body_parameters || {}) }.compact
        req.url "#{@request_client.get_url(request_options: request_options)}/basic-auth"
      end
      JSON.parse(response.body)
    end
  end

  class AsyncBasicAuthClient
    # @return [SeedBasicAuthEnvironmentVariablesClient::AsyncRequestClient]
    attr_reader :request_client

    # @param request_client [SeedBasicAuthEnvironmentVariablesClient::AsyncRequestClient]
    # @return [SeedBasicAuthEnvironmentVariablesClient::AsyncBasicAuthClient]
    def initialize(request_client:)
      @request_client = request_client
    end

    # GET request with basic auth scheme
    #
    # @param request_options [SeedBasicAuthEnvironmentVariablesClient::RequestOptions]
    # @return [Boolean]
    def get_with_basic_auth(request_options: nil)
      Async do
        response = @request_client.conn.get do |req|
          req.options.timeout = request_options.timeout_in_seconds unless request_options&.timeout_in_seconds.nil?
          req.headers["username"] = request_options.username unless request_options&.username.nil?
          req.headers["password"] = request_options.password unless request_options&.password.nil?
          req.headers = { **req.headers, **(request_options&.additional_headers || {}) }.compact
          req.url "#{@request_client.get_url(request_options: request_options)}/basic-auth"
        end
        parsed_json = JSON.parse(response.body)
        parsed_json
      end
    end

    # POST request with basic auth scheme
    #
    # @param request [Object]
    # @param request_options [SeedBasicAuthEnvironmentVariablesClient::RequestOptions]
    # @return [Boolean]
    def post_with_basic_auth(request: nil, request_options: nil)
      Async do
        response = @request_client.conn.post do |req|
          req.options.timeout = request_options.timeout_in_seconds unless request_options&.timeout_in_seconds.nil?
          req.headers["username"] = request_options.username unless request_options&.username.nil?
          req.headers["password"] = request_options.password unless request_options&.password.nil?
          req.headers = { **req.headers, **(request_options&.additional_headers || {}) }.compact
          req.body = { **(request || {}), **(request_options&.additional_body_parameters || {}) }.compact
          req.url "#{@request_client.get_url(request_options: request_options)}/basic-auth"
        end
        parsed_json = JSON.parse(response.body)
        parsed_json
      end
    end
  end
end
