// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: operator/v1alpha1/operator.proto

// Configuration affecting Istio control plane installation version and shape.

package v1alpha1

import (
	bytes "bytes"
	fmt "fmt"
	github_com_gogo_protobuf_jsonpb "github.com/gogo/protobuf/jsonpb"
	proto "github.com/gogo/protobuf/proto"
	_ "istio.io/api/mesh/v1alpha1"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// MarshalJSON is a custom marshaler for IstioOperatorSpec
func (this *IstioOperatorSpec) MarshalJSON() ([]byte, error) {
	str, err := OperatorMarshaler.MarshalToString(this)
	return []byte(str), err
}

// UnmarshalJSON is a custom unmarshaler for IstioOperatorSpec
func (this *IstioOperatorSpec) UnmarshalJSON(b []byte) error {
	return OperatorUnmarshaler.Unmarshal(bytes.NewReader(b), this)
}

// MarshalJSON is a custom marshaler for InstallStatus
func (this *InstallStatus) MarshalJSON() ([]byte, error) {
	str, err := OperatorMarshaler.MarshalToString(this)
	return []byte(str), err
}

// UnmarshalJSON is a custom unmarshaler for InstallStatus
func (this *InstallStatus) UnmarshalJSON(b []byte) error {
	return OperatorUnmarshaler.Unmarshal(bytes.NewReader(b), this)
}

// MarshalJSON is a custom marshaler for InstallStatus_VersionStatus
func (this *InstallStatus_VersionStatus) MarshalJSON() ([]byte, error) {
	str, err := OperatorMarshaler.MarshalToString(this)
	return []byte(str), err
}

// UnmarshalJSON is a custom unmarshaler for InstallStatus_VersionStatus
func (this *InstallStatus_VersionStatus) UnmarshalJSON(b []byte) error {
	return OperatorUnmarshaler.Unmarshal(bytes.NewReader(b), this)
}

var (
	OperatorMarshaler   = &github_com_gogo_protobuf_jsonpb.Marshaler{}
	OperatorUnmarshaler = &github_com_gogo_protobuf_jsonpb.Unmarshaler{}
)
